import imp
from django.shortcuts import render
from django.http import HttpResponse            

def index(request):
    return render(request, 'base.html')

def form(request):
    pass
