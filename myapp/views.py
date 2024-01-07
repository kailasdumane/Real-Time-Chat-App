
from django.shortcuts import render


from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to Home Page!, Currently working on project !!")

def hello(request):
    return HttpResponse("Hello, Django World!")


