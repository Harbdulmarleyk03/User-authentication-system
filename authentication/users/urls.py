from django.urls import path
from .views import RegisterAPIView, LoginAPIView, LogoutAPIView, UserProfileView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("register/", RegisterAPIView.as_view(), name='register'),
    path("login/", LoginAPIView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile-user'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]