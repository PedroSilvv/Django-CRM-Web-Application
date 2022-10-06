from django.shortcuts import render
from django.http import HttpResponse

def registration_form(request):
    return render(request, 'registration.html')