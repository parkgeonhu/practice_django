from rest_framework.response import Response
from .models import Order, Store, Product
from .serializers import OrderSerializer
from rest_framework import viewsets


#viewset은 사용자가 접근하려는 페이지에 필요한 json 통신을 위한 것

class OrderViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

