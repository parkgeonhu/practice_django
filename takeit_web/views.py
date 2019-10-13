from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.response import Response
from .models import Order, Store, Product, Account
from .serializers import OrderSerializer
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


#viewset은 사용자가 접근하려는 페이지에 필요한 json 통신을 위한 것
#프론트 페이지에 어떻게 데이터를 잘 구성해서 전달해줄지가 중요한 부분

class OrderViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    permission_classes = (IsAuthenticated,) 
    authentication_classes = [TokenAuthentication]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderList(generics.ListAPIView):
	serializer_class = OrderSerializer
	permission_classes = (IsAuthenticated,)  
	authentication_classes = [TokenAuthentication]
	
	def get_queryset(self):
		username = self.kwargs['username']
		return Order.objects.filter(orderer=Account.objects.get(uuid=username))