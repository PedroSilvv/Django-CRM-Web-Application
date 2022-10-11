from django.shortcuts import render
from django.http import HttpResponse

def crm_list(request):
    return HttpResponse('lista crm')
