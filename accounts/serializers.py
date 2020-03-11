from rest_framework import serializers
from .models import User

from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


#User serializer

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'email', 'is_agent']

class RegisterSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'password2', 'is_agent']
        extra_kwargs = {'password': {'write_only': True}}

    def save(self):
        account = User(
            email=self.validated_data['email'],
            username=self.validated_data['username']
        )

        password=self.validated_data['password']
        password2=self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({"password": "Passwords must match."})
        
        account.set_password(password)
        account.save()
        return account

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['username', 'is_agent', 'first_name', 'last_name', 'saved_agents', 'id']

class TokenSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Token
        fields = '__all__'


