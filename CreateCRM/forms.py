from dataclasses import fields
from django import forms
from .models import Create_CRM
from django.db import models

class FormCRM(forms.ModelForm):
    class meta:
        model = Create_CRM
        fields = '__all__'