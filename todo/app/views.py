from email import message
from functools import partial
import importlib
from urllib import response
from django.shortcuts import render
# from requests import Response, request
from .models import Todo
from django.http.response import Http404
from rest_framework.views import APIView
from .serializers import Todoserializer
from rest_framework.response import Response

# to kill already use port
# sudo lsof -t -i tcp:8000 | xargs kill -9


class TodoClass(APIView):
    serializer_class = Todoserializer
    def get_object(self, pk):
        try:
            return Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            raise Http404


    def get(self,request, pk = None, formate=None):
        print(request.META)
        if pk:
            data = Todo.objects.get(pk =pk)
            serializer = Todoserializer(data)
        else:
            data = Todo.objects.all()
            serializer = Todoserializer(data, many=True)
        
        response = Response(serializer.data)
        return response

    def post(self, request, format= None):
        data = request.data
        serializer = Todoserializer(data=data)
        if serializer.is_valid():
            # print(serializer.is_valid)
            serializer.save()
            print(serializer.data)
            response = Response()
            response.data = {
                'message': "Post created successfully",
                "data" : serializer.data
            }
            return response
        return Response({"message": "error"})

    def put(self, request, pk):
        todo_update =  Todo.objects.get(pk=pk)
        serializer = Todoserializer(instance=todo_update, data =request.data, partial=True )
        if serializer.is_valid(raise_exception = True):
            serializer.save()
            response = Response()
            response.data = {
                'message' : "Update successfully!",
                'data': serializer.data
            }
            return response
        return Response({'message':'error'})

    def delete(self, pk, fomate= None):
        delete_todo = Todo.objects.get(pk = pk)
        delete_todo.delete()

        return Response({'message':'Delete successfully !'})





        