from unicodedata import name
from django.urls import path  
from . import views

urlpatterns = [
    path('em-processo/', views.crm_list_processo, name='crmlist-processo'),
    path('finalizadas/', views.crm_list_finalizada, name='crmlist-finalizadas'),
    path('pendentes/', views.crm_list_pendente, name='crmlist-pendentes'),
    path('crmdetail/<int:crm_id>/', views.crm_detail, name='crm-detail'),
    path('meus-projetos/em-processo/', views.minhas_crm_emprocesso, name='mycrmlist-processo'),
    path('busca/', views.busca, name='search')
]

