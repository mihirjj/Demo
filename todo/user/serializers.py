from asyncore import write
from genericpath import exists
from tkinter import E

from requests import request
from rest_framework import serializers
from .models import Profile, User

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class RegistrationSerializer(serializers.ModelSerializer):
    profiles = ProfileSerializer(required=False)

    class Meta:
        model = User
        fields = ['email', 'full_name', 'password', 'profiles']
        extra_kwargs = {'password':{'write_only':True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profiles')
        user = User.objects.create_user(**validated_data)
        # user.set_password(validated_data['password'])
        Profile.objects.create(
            user=user,
            phone=profile_data['phone'],
            location = profile_data['location'],
            gender = profile_data['gender'],
            profile_picture=profile_data['profile_picture']
        )
        # print(user)
        return user

from django.contrib.auth import authenticate

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 're_password']
        extra_kwargs = {'password':{'write_only':True}}

    def validate(self, validated_data):
        email = validated_data.pop('email')
        password = validated_data.pop('password')
        user = authenticate(email=email, password=password)
        if user is None:
            print("Logged in ", user)
        else:
            print("Error on code", user)
