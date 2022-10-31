from multiprocessing import context
from winreg import CreateKeyEx
from django.shortcuts import render
from django.http import HttpResponse
import random
from unicodedata import digit
from faker import Faker
from CreateCRM.models import Create_CRM
from django.contrib.auth.decorators import login_required

fake = Faker()

def rand_ratio():
    return random.randint()

def create_random_CRM():
    return {
        'id' : fake.random_number(digits=4),
        'data' : fake.date(),
        'colaboradores' : fake.random_number(1,8),
    }

#print(fake.random_number(digits=4))
#print(fake.date())


@login_required(login_url='/')
def crm_list_processo(request):    
    return render(request, 'crm_list.html', context={
        'qts_crm' : Create_CRM.objects.filter(status_crm='em processo'),
        'status_crm' : 'processo'
    })

@login_required(login_url='/')
def crm_list_finalizada(request):
    return render(request, 'crm_list.html', context={
        'qts_crm' : Create_CRM.objects.filter(status_crm='finalizadas'),
        'status_crm' : 'finalizada'
    })

@login_required(login_url='/')
def crm_list_pendente(request):
    return render(request, 'crm_list.html', context={
        'qts_crm' : Create_CRM.objects.filter(status_crm='pendentes'),
        'status_crm' : 'pendente'
        
    })


@login_required(login_url='/')
def crm_detail(request, crm_id):

    crm = Create_CRM.objects.get(id=crm_id)

    return render(request, 'crm_detail.html', {
        'crm' : crm,
        'setores' : crm.setor.all()        
    })

def busca(request):
    termo = request.GET.get("termo")
    qts_crm = Create_CRM.objects.order_by('-id').filter(
        id__icontains=termo
    )

    return render(request, 'busca.html', context={
        'qts_crm' : qts_crm,
        'status_crm' : 'processo'
    })

def minhas_crm_emprocesso(request):
    pass