# myapp/urls.py
from django.urls import path
from .views import hello,home

urlpatterns = [
    path('',home,name="home"),
    path('hello/', hello, name='hello'),
]

