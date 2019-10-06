from django.conf.urls import url
from . import views
from django.conf import settings
from django.contrib.auth.views import LogoutView


urlpatterns =[
    url(r'^signup$', views.signup, name='signup'),
    url(r'^login/$', views.login, name='login'),
   # url(r'^login/$', auth_view.login, name='login',
   #     kwargs={
   #         'authentication_form' : LoginForm,
   #         'template_name' : 'accounts/login_form.html'
   #     }),
    url(r'^logout/', LogoutView.as_view(), name="logout"),
    url(r'^profile/$', views.profile, name='profile'),
]