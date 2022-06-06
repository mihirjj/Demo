from functools import partial
import re
from django.shortcuts import render
# from requests import request
from django.http import JsonResponse
from rest_framework.generics import CreateAPIView  
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegistrationSerializer
# Create your views here.
from .models import User,Profile
from .serializers import RegistrationSerializer,ProfileSerializer

class RegistrationView(CreateAPIView):
    serializer_class = RegistrationSerializer
    # queryset = User.objects.all()

    def get(self,request):
        data = User.objects.all()
        serializer = RegistrationSerializer(data, many = True)
        print(type(serializer))
        return Response({'serializer': serializer.data})

    def post(self,request, format=None):
        data = request.data
        if User.objects.filter(email = data['email']).exists():
            message = "You Already exists"
            return Response({'message': message})
        else:
            serialzer = RegistrationSerializer(data = data, partial= True)
            print(data)
            if serialzer.is_valid(raise_exception = True):
                serialzer.save()
                print(data)
                response = Response()
                response.data = {
                    'message': 'User Successfully Registered',
                    'data': serialzer.data,
                    'status': status.HTTP_201_CREATED
                }
                # print(type(response))                 
                return response
        return Response({'message': 'ERRRORROORRR'})

