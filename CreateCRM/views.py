from tkinter import N
from django.shortcuts import render
from django.http import HttpResponse            
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_crm
from django.contrib.auth.decorators import login_required

from CreateCRM.forms import CreateCRMForm
from .models import Create_CRM
from registration.models import CustomUser, Setor

@login_required(login_url='/')
def createcrm(request):

    crm = Create_CRM.objects.filter(
        solicitante=request.user
    ).first()

    form = CreateCRMForm(
        data = request.POST or None,
        instance=crm
    )

    return render(request, 'createcrm.html', context={
        'form' : form})


