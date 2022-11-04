from unicodedata import name
from django.urls import path  
from . import views

urlpatterns = [
    path('em-processo/', views.crm_list_processo, name='crmlist-processo'),
    path('finalizadas/', views.crm_list_finalizada, name='crmlist-finalizadas'),
    path('pendentes/', views.crm_list_pendente, name='crmlist-pendentes'),
    path('crmdetail/<int:crm_id>/<int:crm_versao>', views.crm_detail, name='crm-detail'),
    path('meus-projetos/pendentes/', views.minhas_crm_pendente, name='mycrmlist-pendentes'),
    path('meus-projetos/em-processo/', views.minhas_crm_processo, name='mycrmlist-processo'),
    path('meus-projetos/finalizadas/', views.minhas_crm_finalizada, name='mycrmlist-finalizadas'),
    path('editar-crm/<int:crm_id>/<int:crm_versao>', views.editar_crm, name='editar_crm'),
    path('update-crm/<int:crm_id>/<int:crm_versao>', views.update_crm, name='update_crm'),
    path('arquivar-crm/<int:crm_id>/<int:crm_versao>', views.arquivar_crm, name='arquivar_crm'),
    path('busca/', views.busca, name='search')
]

