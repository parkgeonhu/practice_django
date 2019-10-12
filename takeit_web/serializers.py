from .models import Order, OrderItem, Store
from rest_framework import serializers

# from django.contrib.auth.models import User

# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     url = serializers.HyperlinkedIdentityField(view_name="user-detail")
#     class Meta:
#         model = User
#         fields = ('url', 'username', 'email', 'is_staff')
        

# class OrderItmemsField(serializers.RelatedField):
#     def to_representation(self, value):
#         return f'{value.product.name}@{value.order.store.name} (in {value.order.order_number})'
    
#     def to_internal_value(self, data):
#         try:
#             try:
#                 return User.objects.get(username=data)
#             except KeyError:
#                 raise serializers.ValidationError(
#                     'id is a required field.'
#                 )
#             except ValueError:
#                 raise serializers.ValidationError(
#                     'id must be an integer.'
#                 )
#         except User.DoesNotExist:
#             raise serializers.ValidationError(
#             'Obj does not exist.'
#             )    


# class StoreSerializer(serializers.Serializer):
#     uuid = serializers.CharField(max_length=100)
    
# class UserSerializer(serializers.Serializer):
#     username = serializers.CharField(max_length=100)

# class ProductSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=100)
    

class OrderItemSerializer(serializers.ModelSerializer):
    # def to_representation(self, value):
    #     value.product=ProductSerializer()
    #     return 'Product : %s, options : %s' % (value.product, value.options)
    product=serializers.SlugRelatedField(slug_field='name', read_only=True)
    
    class Meta:
        model = OrderItem
        fields = ['product','options']
    


class OrderSerializer(serializers.ModelSerializer):
    # orderitems = OrderItemsField(queryset=User.objects.all(), many=True)
    orderer = serializers.SlugRelatedField(slug_field='uuid', read_only=True)
    store= serializers.SlugRelatedField(slug_field='uuid', read_only=True)
    order_items = OrderItemSerializer(many=True)

    
    class Meta:
        model = Order
        fields = '__all__' 
    # class Meta:
    #     model = Event
    
    
    #     fields = ('first_name', 'last_name')