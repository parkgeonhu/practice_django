from django.db import models
from django.contrib.auth.models import User

# import datetime
# from pytz import timezone

class Person(models.Model):
    

    def __str__(self):
        return self.phone

    @property
    def is_store_owner(self):
        try:
            return self.store is not None
        except Store.DoesNotExist:
            return False


class Store(models.Model):

    name = models.CharField(max_length=64, help_text='가게 이름')
    street_address = models.CharField(max_length=128, help_text='도로명 주소(신 주소)')
    place = models.CharField(max_length=64, help_text='숭실대학교 학생회관 4층')
    # location = gis_models.PointField(geography=True, help_text='Use POINT(lng lat) format')
    owner = models.OneToOneField(User, models.CASCADE, related_name='store')
    owner_phone = models.CharField(max_length=20, help_text='점주 전화번호')
    note = models.TextField(help_text='비고 등 기타 메모', blank=True)
    is_opened = models.BooleanField(default=False)
    using_point_system = models.BooleanField(default=True)
    store_detail = models.TextField(help_text="가게 영업 시간, 휴무 등의 상세정보, [{'key': 'value'}] 형태", default=list, blank=True)
    
    def __str__(self):
        return self.name




# Create your models here.
class Product(models.Model):
    store = models.ForeignKey(Store, models.CASCADE, related_name='products')
    name = models.CharField(max_length=64)
    priority = models.PositiveIntegerField(default=0, help_text="앱에 표시될 때의 우선순위")
    description = models.CharField(max_length=128, blank=True)
    default_price = models.IntegerField(default=3000)
    category = models.CharField(max_length=16)
    options = models.TextField(help_text='이용 가능한 옵션', default=list, blank=True)

    def __str__(self):
        return f'{self.name}@{self.store.name}'
    


class OrderItem(models.Model):
    product = models.ForeignKey(Product, models.CASCADE)
    options = models.TextField(help_text='이용 가능한 옵션')
    order = models.ForeignKey('Order', models.CASCADE, related_name='order_items')

    def __str__(self):
        return f'{self.product.name}@{self.order.store.name} (in {self.order.order_number})'

    
# def now_korea() -> datetime.datetime:
#     return datetime.datetime.now(timezone('Asia/Seoul'))

class OrderStatus:
    FAILURE_PAYMENT = 'FAILURE_PAYMENT'
    WAITING_PAYMENT = 'WAITING_PAYMENT'
    NEW = 'NEW'
    REJECTED = 'REJECTED'
    IN_PROGRESS = 'IN_PROGRESS'
    MANUFACTURED = 'MANUFACTURED'
    DELIVERED = 'DELIVERED'

    
ORDER_STATUS = (
    (OrderStatus.FAILURE_PAYMENT, '결제 실패'),
    (OrderStatus.WAITING_PAYMENT, '결제 대기중'),
    (OrderStatus.NEW, '새 주문'),
    (OrderStatus.REJECTED, '주문 거절'),
    (OrderStatus.IN_PROGRESS, '제조 중'),
    (OrderStatus.MANUFACTURED, '제조 완료'),
    (OrderStatus.DELIVERED, '전달 완료'),
)


    
class Order(models.Model):
    orderer = models.ForeignKey(User, on_delete=models.PROTECT, related_name='orders')
    store = models.ForeignKey(Store, on_delete=models.PROTECT, related_name='orders')
    status = models.CharField(max_length=32, choices=ORDER_STATUS,
                              default=OrderStatus.WAITING_PAYMENT, help_text='진행 상황')
    order_number = models.CharField(max_length=16, help_text='A-01 ~ Z-999')
    # Range of PositiveSmallIntegerField: 0 ~ 32767
    grand_total = models.IntegerField(help_text='총 합계(결제 금액)')
    name = models.CharField(max_length=31, help_text='커피 외 n건')
    orderer_request = models.CharField(max_length=500, help_text='고객님 요청사항')

    def __str__(self):
        return f'{self.order_number}@{self.store.name}, {self.name}'

    # def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
    #     if not self.id:
    #         # only new object
    #         try:
    #             today = now_korea().date()
    #             latest_order = Order.objects.filter(
    #                 created_at__year=today.year,
    #                 created_at__month=today.month,
    #                 created_at__day=today.day,
    #             ).filter(store=self.store).latest('order_number')
    #             order_number = next_order_number(latest_order.order_number)
    #         except Order.DoesNotExist:  # raise by .latest('order_number')
    #             order_number = 'A-01'
    #         self.order_number = order_number
    #     super(Order, self).save(force_insert, force_update, using, update_fields)




