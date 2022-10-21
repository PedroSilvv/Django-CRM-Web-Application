from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
import random
from unicodedata import digit
from faker import Faker
from CreateCRM.models import Create_CRM

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

def crm_list_processo(request):
    return render(request, 'crm_list.html', context={
        'qts_crm' : Create_CRM.objects.all(),
        'crm' : Create_CRM.objects,
    })

def crm_list_finalizada(request):
    return render(request, 'crm_list.html', context={
        'qts_crm' : [create_random_CRM() for i in range(2)],
        'crm' : create_random_CRM,
    })


def crm_list_pendente(request):
    return render(request, 'crm_list.html', context={
        'qts_crm' : [create_random_CRM() for p in range(4)],
        'crm' : create_random_CRM,
    })



def crm_detail(request):
    return render(request, 'crm_detail.html')



