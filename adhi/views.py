from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.urls import path

def home(request):
    return HttpResponse("<h1 style='color: green;'>Welcome to Django</h1>")
