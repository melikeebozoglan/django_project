from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
    return HttpResponse("<h1>index sayfası</h1>")
