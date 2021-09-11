from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def harish(request):
    return HttpResponse('hii harish')

def home(request):
    return HttpResponse('hello home')