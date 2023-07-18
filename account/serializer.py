from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name')


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name')

    def create(self, validate_data):
        user = User.objects.create_user(
            email=validate_data['email'],
            password=validate_data['password'],
            first_name=validate_data.get('first_name'),
            last_name=validate_data.get('last_name'),
        )
        return user

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self,attrs):
        data = super(CustomTokenObtainPairSerializer,self).validate(attrs)

        user = UserSerializer(self.user)
        data.update({'user':user.data})
        return data
