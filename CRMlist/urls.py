from unicodedata import name
from django.urls import path  
from . import views

urlpatterns = [
    path('', views.crm_list_processo, name='crmlist'),
    path('finalizadas/', views.crm_list_finalizada, name='crmlist-finalizadas'),
    path('pendentes/', views.crm_list_pendente, name='crmlist-pendentes'),
    path('crmdetail/', views.crm_detail, name='crm-detail'),
]

