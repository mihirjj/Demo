from django.contrib import admin
from django.urls import path, include
from .views import RegistrationView

urlpatterns = [
    path('signup', RegistrationView.as_view()),
    # path('', TodoClass.as_view())
]