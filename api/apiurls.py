from django.urls import path
from api import apiviews
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


app_name = 'api'

urlpatterns = [
    path('auth/login/', apiviews.LoginAPI.as_view(), name='auth-login'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='auth-token-refresh'),
    path('lookup/addr', apiviews.AddrAPI.as_view(), name='lookup-addr'),

    path('auth/register/', apiviews.RegisterAPI.as_view(), name='auth-register'),
    path('users', apiviews.UsersAPI.as_view(), name='users'),
]
