from django.urls import re_path, path
from .views import OrderList


urlpatterns = [
    # path('', views.post_list, name='post_list'),
    re_path('^order/(?P<username>.+)/$', OrderList.as_view()),
    
]