from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import login, authenticate
from rest_framework import exceptions
from rest_framework.authtoken.models import Token

class AuthToken(APIView):
	def post(self, request):
		username=request.data.get('username')
		password=request.data.get('password')
		user=authenticate(username=username,password=password)
		
		if user:
			token, created=Token.objects.get_or_create(user=user)
			data={'token' : token.key}
			return Response(data)
		
		raise exceptions.AuthenticationFailed('인증 정보 x')

class AuthenticationTest(APIView):
	def get(self, request):
		if request.user.is_authenticated:
			return Response("성공")
		raise exceptions.NotAuthenticated('아니다')


# from django.contrib.auth.models import User
# from rest_framework import viewsets
# from rest_framework.response import Response
# from rest_framework.views import APIView    
# from rest_framework.permissions import IsAuthenticated
# from rest_framework import exceptions
# from rest_framework import authentication
# from django.contrib.auth import authenticate, get_user_model
# from rest_framework.authentication import BasicAuthentication, 
# SessionAuthentication


# class ExampleAuthentication(authentication.BaseAuthentication):

#     def authenticate(self, request):

#         # Get the username and password
#         username = request.data.get('username', None)
#         password = request.data.get('password', None)

#         if not username or not password:
#             raise exceptions.AuthenticationFailed(_('No credentials provided.'))

#         credentials = {
#             get_user_model().USERNAME_FIELD: username,
#             'password': password
#         }

#         user = authenticate(**credentials)

#         if user is None:
#             raise exceptions.AuthenticationFailed(_('Invalid username/password.'))

#         if not user.is_active:
#             raise exceptions.AuthenticationFailed(_('User inactive or deleted.'))


#     return (user, None)  # authentication successful


# class MyView(APIView):
#     authentication_classes = (SessionAuthentication, ExampleAuthentication,)
#     permission_classes = (IsAuthenticated,)

#     def post(self, request, format=None):    
#         content = {
#             'user': unicode(request.user),
#             'auth': unicode(request.auth),  # None
#         }
#         return Response(content)