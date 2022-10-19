from email.policy import default
from pyexpat import model
from random import choices
from statistics import mode
from unittest import defaultTestLoader
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser

class Setor(models.Model):

    nome = models.CharField(max_length=100)
    is_ti = models.BooleanField(default=False)

    def __str__(self):
        return self.nome

class CustomUser(AbstractUser):
    
    email = models.EmailField(unique=True)
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.username

