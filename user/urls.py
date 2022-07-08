from django.contrib import admin
from django.urls import path, include
from .views import SignUpView,SpartaTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('sign-up', SignUpView.as_view()),
    path('api/token/', SpartaTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/', TokenRefreshView(), name='token_refresh'),
]
