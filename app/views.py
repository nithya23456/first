from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    return HttpResponse('<marquee><i><h1>This is my frst FBV.. </h1></i></marquee>')