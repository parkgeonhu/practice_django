from .models import Order
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


class StoreSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    
class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    # orderitems = OrderItemsField(queryset=User.objects.all(), many=True)
    orderer=UserSerializer()
    store=StoreSerializer()
    
    class Meta:
        model = Order
        fields = '__all__' 
    # class Meta:
    #     model = Event
    
    
    #     fields = ('first_name', 'last_name')