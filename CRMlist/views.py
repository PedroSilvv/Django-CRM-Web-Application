from multiprocessing import context
from winreg import CreateKeyEx
from django.shortcuts import render
from django.http import HttpResponse
import random
from unicodedata import digit
from faker import Faker
from CreateCRM.models import Create_CRM
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Value
from django.db.models.functions import Concat

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
        'qts_crm' : Create_CRM.objects.filter(status_crm='em processo', mostrar_crm=True),
        'status_crm' : 'processo'
    })

@login_required(login_url='/')
def crm_list_finalizada(request):
    return render(request, 'crm_list.html', context={
        'qts_crm' : Create_CRM.objects.filter(status_crm='finalizadas', mostrar_crm=True),
        'status_crm' : 'finalizada'
    })

@login_required(login_url='/')
def crm_list_pendente(request):
    return render(request, 'crm_list.html', context={
        'qts_crm' : Create_CRM.objects.filter(status_crm='pendentes', mostrar_crm=True),
        'status_crm' : 'pendente'
        
    })


@login_required(login_url='/')
def crm_detail(request, crm_id):

    crm = Create_CRM.objects.get(id=crm_id)
    
    if request.method == 'POST':
        if request.POST['arquivar']:
                crm.mostrar_crm = False
                return render(request, 'crm_list.html')

    return render(request, 'crm_detail.html', {
        'crm' : crm,
        'setores' : crm.setor.all(),
    })


def busca(request):
    termo = request.GET.get("termo")
    qts_crm = Create_CRM.objects.order_by('-id').filter(
        Q(id__icontains=termo) | Q(data_criacao__icontains=termo) 
    )

    return render(request, 'busca.html', context={
        'qts_crm' : qts_crm,
    })

@login_required(login_url='/')
def minhas_crm_pendente(request):
    usuario = request.user 
    setor_usuario = usuario.setor
    qts_crm = Create_CRM.objects.filter(status_crm='pendentes', setor=setor_usuario, mostrar_crm=True)

    return render(request, 'my_crm_list.html', context={
        'qts_crm' : qts_crm,
        'status_crm' : 'pendente'
    })


@login_required(login_url='/')
def minhas_crm_processo(request):
    usuario = request.user 
    setor_usuario = usuario.setor
    qts_crm = Create_CRM.objects.filter(status_crm='em processo', setor=setor_usuario, mostrar_crm=True)

    return render(request, 'my_crm_list.html', context={
        'qts_crm' : qts_crm,
        'status_crm' : 'processo'
    })


@login_required(login_url='/')
def minhas_crm_finalizada(request):
    usuario = request.user 
    setor_usuario = usuario.setor
    qts_crm = Create_CRM.objects.filter(status_crm='finalizadas', setor=setor_usuario, mostrar_crm=True)

    return render(request, 'my_crm_list.html', context={
        'qts_crm' : qts_crm,
        'status_crm' : 'finalizada'
    })


@login_required(login_url='/')
def crm_arquivada(request):

    qts_crm = Create_CRM.objects.filter(mostrar_crm=False)

    return render(request, 'my.crm_list.html', context={
        'qts_crm' : qts_crm
    })


