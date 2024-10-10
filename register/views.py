from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("Here to Register")

def register_name_password(request):
    return HttpResponse("Enter your password")