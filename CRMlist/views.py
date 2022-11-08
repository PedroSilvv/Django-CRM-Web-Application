from multiprocessing import context
from winreg import CreateKeyEx
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
import random
from unicodedata import digit
from faker import Faker
from CreateCRM.models import Create_CRM, Feedback
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
    
    user = request.user
    setor_usuario = request.user.setor
    crm = Create_CRM.objects.get(id=crm_id, versao=crm_versao)
    aceites = Feedback.objects.filter(crm=crm_id, versao_crm=crm_versao).all()
    total_setores = crm.setor.all()
    lista_aceites = []
    lista_setores = []

    for x in total_setores:
        lista_setores.append(x)

    for x in aceites:
        lista_aceites.append(x)
    
    print(lista_aceites)
    print(lista_setores)

    try:
        aceite = Feedback.objects.get(colaborador=user, crm=crm_id, versao_crm=crm_versao)
    except:
        aceite = False

    return render(request, 'crm_detail.html', context={
        'crm' : crm,
        'setores' : crm.setor.all(),
        'aceites' : aceites,
        'aceite' : aceite,
        'lista_setores' : len(lista_setores),
        'lista_aceites' : len(lista_aceites),
        'setor_usuario' : request.user.setor
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
        Q(id=termo) | Q(data_criacao__icontains=termo)
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

    qts_crm = Create_CRM.objects.filter(status_crm='finalizadas')

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

        Create_CRM.objects.filter(id=crm_id, versao=crm_versao).update(status_crm='finalizadas')
        return render(request, 'home.html')
        


def versoes_anteriores(request, crm_id):
    
    return render(request, 'crm_list.html', context={
        'qts_crm' : Create_CRM.objects.filter(id=crm_id),
        'status_crm' : 'Versões'
    })


def feedback_positivo(request, crm_id, crm_versao):

    colaborador = request.user
    crm = Create_CRM.objects.get(id=crm_id, versao=crm_versao)
    versao = crm.versao

    Feedback.objects.get_or_create(colaborador=colaborador, crm=crm, versao_crm=versao, justificativa='...')
    
    Feedback.objects.filter(colaborador=colaborador, crm=crm, versao_crm=versao).update(resposta=True)

    return render(request, 'my_crm_list.html')


def rejeite(request, crm_id, crm_versao):
    colaborador = request.user 
    crm = Create_CRM.objects.get(id=crm_id, versao=crm_versao)
    versao = crm.versao

    if request.method == "POST":

        justificativa = request.POST.get('rejeite')
        
        Feedback.objects.filter(colaborador=colaborador, crm=crm, versao_crm=versao).update(justificativa=justificativa)
        return render(request, 'home.html', context={
            'crm' : crm
        })


def feedback_negativo(request, crm_id, crm_versao):

    colaborador = request.user 
    crm = Create_CRM.objects.get(id=crm_id, versao=crm_versao)
    versao = crm.versao

    Feedback.objects.get_or_create(colaborador=colaborador, crm=crm, versao_crm=versao, justificativa='Justificativa')
    
    Feedback.objects.filter(colaborador=colaborador, crm=crm, versao_crm=versao).update(resposta=False)
    return render(request, 'rejeite.html', context={
        'crm' : crm
    })

def flag_ti(request, crm_id, crm_versao):

    Create_CRM.objects.filter(id=crm_id, versao=crm_versao).update(status_crm='em processo')

    return render(request, 'home.html')


def respostas_crm(request):

    user = request.user
    crm = Create_CRM.objects.filter(solicitante=user)

    #Feedback.objects.filter(crm=crm)

    return render(request, 'respostas_crm.html', context={
        'qts_crm' : crm,
    })


def mostrar_respostas(request, crm_id, crm_versao):

    crm = Create_CRM.objects.get(id=crm_id, versao=crm_versao)
    versao = crm.versao
    feed = Feedback.objects.filter(crm=crm, versao_crm=versao)

    return render(request, 'resposta-view.html', context={
        'crm' : crm,
        'feed' : feed
    })

    