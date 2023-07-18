from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializer import RegisterSerializer, UserSerializer, CustomTokenObtainPairSerializer


# Create your views here.
class Register(APIView):
    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        user = serializer.create(serializer.validated_data)
        refresh = RefreshToken.for_user(user)
        user = UserSerializer(user)
        data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': user.data
        }
        return Response(data,status=status.HTTP_201_CREATED)

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


