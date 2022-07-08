import json
import datetime
from django.contrib.auth.hashers import make_password
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status


from django.contrib.auth import login, authenticate, logout

from .models import User, UserLog, UserType
from user.jwt_claim_serializers import SpartaTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class SignUpView(APIView):

    permission_classes = [permissions.AllowAny]
    # 회원 가입
    def post(self, request):
        # data = json.loads(request.body)
        user_type = request.data.get('user_type', None)
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        # User.objects.create(email=email, password=password)
        usertype = UserType.objects.get(user_type = user_type)

        # passcode = make_password(password)
        # print("usertype=", end=""), print(usertype)
        # User(email=email, password=make_password(password)).save()
        User(user_type=usertype, email=email, password=make_password(password)).save()

        return Response(status=status.HTTP_200_OK)


class SpartaTokenObtainPairView(TokenObtainPairView):
    serializer_class = SpartaTokenObtainPairSerializer