from multiprocessing import context
from winreg import CreateKeyEx
from django.shortcuts import render
from django.http import HttpResponse, Http404
import random
from unicodedata import digit
from faker import Faker
from CreateCRM.models import Create_CRM
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Value
from django.conf import settings
import os
from registration.models import Setor


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
def crm_detail(request, crm_id, crm_versao):
    
    crm = Create_CRM.objects.get(id=crm_id, versao=crm_versao)
 
    return render(request, 'crm_detail.html', {
        'crm' : crm,
        'setores' : crm.setor.all()
    })


def download_files(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response=HttpResponse(fh.read(), content_type='application/file')
            response['Content-Disposition']='inline;filename'+os.path.basename(file_path)
            return response

    raise Http404



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

@login_required(login_url='/')
def editar_crm(request, crm_id, crm_versao):

    crm = Create_CRM.objects.get(id=crm_id, versao=crm_versao)

    return render(request, 'update_crm.html', context={
        'crm' : crm,
        'setores' : crm.setor.all(),
        'all_setores' : Setor.objects.values
    })

@login_required(login_url='/')
def update_crm(request, crm_id, crm_versao):
    
    try:
        solicitante = request.user
        data = request.POST.get("data")
        empresa = request.POST.get("empresa")
        file = request.FILES.get('upload')
        setores = request.POST.get('setores')
        descricao = request.POST.get('descricao')
        justificativa = request.POST.get('justificativa')
        objetivo = request.POST.get('objetivo')

        crm = Create_CRM.objects.create(id=crm_id, versao=crm_versao+1, solicitante=solicitante, data_criacao=data, empresa=empresa,
        file=file, descricao=descricao, justificativa=justificativa, objetivo=objetivo)

        crm.setor.add(setores)
        crm.save()

        return render(request, 'home.html')

    except :
        return render(request, 'home.html')



def arquivar_crm(request, crm_id, crm_versao):

        Create_CRM.objects.filter(id=crm_id, versao=crm_versao).update(mostrar_crm=False)
        return render(request, 'home.html')
        



