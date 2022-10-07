from wsgiref.util import request_uri
from django.shortcuts import render
from django.http import HttpResponse            
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_crm
from django.contrib.auth.decorators import login_required

@login_required(login_url='')
def homepage(request):
    return render(request, 'home.html')
