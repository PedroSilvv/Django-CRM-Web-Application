from dataclasses import fields
from django import forms
from .models import Create_CRM

class CreateCRMForm(forms.ModelForm):
    
    class meta:
        model = Create_CRM
        fields = 'data_criacao', 'descricao', 'objetivo', 'justificativa', 'dependencia', 'empresa', 'status_crm', \
                 'versao', 'file' 