from django.contrib import admin
from django.urls import path, include
from .views import SignUpView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('sign-up', SignUpView.as_view()),

]
