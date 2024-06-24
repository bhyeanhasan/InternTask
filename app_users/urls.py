from django.urls import path
from .views import (
    UserRegisterAPIView,
    UserLoginAPIView,
    UserDetailsAPIView,
    UserUpdateAPIView,
    UserDeleteAPIView,
)

urlpatterns = [
    path('register/', UserRegisterAPIView.as_view(), name='user-register'),
    path('login/', UserLoginAPIView.as_view(), name='user-login'),
    path('<id>/', UserDetailsAPIView.as_view(), name='user-detail'),
    path('<id>/update/', UserUpdateAPIView.as_view(), name='user-update'),
    path('<id>/delete/', UserDeleteAPIView.as_view(), name='user-delete'),
]
