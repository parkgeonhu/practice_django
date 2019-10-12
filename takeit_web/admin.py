from django.contrib import admin


from .models import Product, Store, Order, OrderItem, Account

# Register your models here.
admin.site.register(Product)
admin.site.register(Store)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(Account)
