from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.


def Homepage(request):
    return render(request, 'index.html')


def Analysis(request):
    return render(request, 'MaBussines.html')


def Addproduct (request):
    models.Product