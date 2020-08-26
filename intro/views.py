from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'slide.html')

def slideNext(request):
    return render(request, 'slideNext.html')
