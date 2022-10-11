from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
import random
from unicodedata import digit
from faker import Faker

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

def crm_list(request):
    return render(request, 'crm_list.html', context={
        'qts_crm' : [create_random_CRM() for _ in range(12)],
        'crm' : create_random_CRM(),
    })



