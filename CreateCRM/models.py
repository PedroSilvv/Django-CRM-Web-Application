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


    id = models.AutoField(primary_key=True)
    versao = models.IntegerField(null=False, default=1)
    data_criacao = models.DateField()
    descricao = models.TextField()
    objetivo = models.TextField()
    justificativa = models.TextField()
    dependencia = models.BooleanField(default=False)
    mostrar_crm = models.BooleanField(default=True)
    empresa = models.CharField(max_length=50)
    status_crm = models.CharField(max_length=50, choices=STATUS, default='Pendentes')
    complexidade_crm = models.CharField(max_length=50, choices=COMPLEXIDADE, blank=True)
    file = models.FileField(blank=True, upload_to='files/%Y/%m/',)
    solicitante = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    setor = models.ManyToManyField(Setor, related_name='setores_crm')

    class Meta:
        unique_together = (('id', 'versao'),)

    def __str__(self):
        return f'CRM - {self.id}'



class Feedback(models.Model):

    colaborador = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    crm = models.ForeignKey(Create_CRM, on_delete=models.CASCADE, related_name='crm')
    versao_crm = models.IntegerField()
    resposta = models.BooleanField(default=False)
    justificativa = models.TextField()