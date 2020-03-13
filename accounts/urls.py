from django.urls import path, include
from .api import registration_view, UserDetail, TokenDetail
from .google import google_api_send_email
from rest_framework.authtoken.views import obtain_auth_token


app_name='accounts'

urlpatterns = [
    path('register', registration_view, name='register'),
    path('login', obtain_auth_token, name='login'),
    path('google', google_api_send_email, name='google'),
    path('token/<key>', TokenDetail.as_view(), name='token_detail'),
    path('user/<int:pk>', UserDetail.as_view(), name='user_detail')
    
]