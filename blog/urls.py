from django.urls import re_path, path
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('signup', views.signup, name='signup'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    path('comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
    path('^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    re_path('^payment/$', views.payment, name='payment'),
]