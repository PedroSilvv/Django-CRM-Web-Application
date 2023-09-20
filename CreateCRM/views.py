from audioop import add
from tkinter import N
from typing import Set
from django.shortcuts import render
from django.http import HttpResponse            
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_crm
from django.contrib.auth.decorators import login_required
from .models import Create_CRM
from registration.models import CustomUser, Setor

def converter_boolean(valor_dependencia):
    if valor_dependencia == 'True':
        return True

    elif valor_dependencia == 'False':
        return False


@login_required(login_url='/')
def createcrm(request):

    if request.method == "GET":
        return render(request, 'createcrm.html', context={
            "setores" : Setor.objects.values,
            'setor' : Setor.objects,
            'solicitante' : request.user,
        })
    else:
        solicitante = request.user
        data = request.POST.get('data')
        empresa = request.POST.get('empresa')
        versao = request.POST.get('versao')
        file = request.FILES.get('upload')
        setores = request.POST.getlist('setores')
        descricao = request.POST.get('descricao')
        justificativa = request.POST.get('justificativa')
        objetivo = request.POST.get('objetivo')
        dependencia = request.POST.get('dependencia')
        complexidade = request.POST.get('complexidade')
        
        dependencia_convertido = converter_boolean(dependencia)

        crm = Create_CRM.objects.create(solicitante=solicitante, empresa=empresa, versao=1, file=file, 
                                        descricao=descricao, justificativa=justificativa, objetivo=objetivo,
                                        dependencia=dependencia_convertido, complexidade_crm=complexidade)
        
        for x in setores:
            crm.setor.add(x)

        crm.save()

        return render(request, 'home.html')
    



    