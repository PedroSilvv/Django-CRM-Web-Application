from distutils.command.upload import upload
from email.policy import default
from random import choices
from django.db import models
from registration.models import CustomUser, Setor
from unittest.util import _MAX_LENGTH


class Create_CRM(models.Model):

    STATUS = (
        ('Em processo', 'em processo'),
        ('Finalizadas','finalizadas'),
        ('Pendentes', 'pendentes')
    )

    COMPLEXIDADE = (
        ('Alta', 'alta'),
        ('Media','media'),
        ('Baixa', 'baixa')
    )
    
    status_crm = models.CharField(max_length=50, choices=STATUS, default='Pendentes')
    data_criacao = models.DateField()
    descricao = models.TextField()
    objetivo = models.TextField()
    justificativa = models.TextField()
    dependencia = models.BooleanField(default=False)
    mostrar_crm = models.BooleanField(default=True)
    empresa = models.CharField(max_length=50)
    versao = models.IntegerField(default=1)
    status_crm = models.CharField(max_length=50, choices=STATUS, default='Pendentes')
    complexidade_crm = models.CharField(max_length=50, choices=COMPLEXIDADE, blank=True)
    file = models.FileField(blank=True, upload_to='files/%Y/%m/',)
    solicitante = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    setor = models.ManyToManyField(Setor, related_name='setores_crm')

    def __str__(self):
        return f'CRM - {self.id}'

