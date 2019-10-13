from django.urls import re_path, path
from .views import AuthToken, AuthenticationTest


urlpatterns = [
    # path('', views.post_list, name='post_list'),
    path('token-test', AuthenticationTest.as_view()),
    path('token', AuthToken.as_view()),
]