from django.contrib import admin
from django.urls import path, include
from .views import TodoClass

urlpatterns = [
    path('todo', TodoClass.as_view()),
    path('todo/<str:pk>', TodoClass.as_view())
]