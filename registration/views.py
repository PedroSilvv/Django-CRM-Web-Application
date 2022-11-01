import email
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import CustomUser, Setor

def registration(request):
    if request.method == "GET":
        return render(request, 'registration.html', context={
            "setores" : Setor.objects.values,
            'setor' : Setor.objects
        })

    else:
        nome = request.POST.get("nome")
        email = request.POST.get("email")    
        matricula = request.POST.get("matricula")
        setor_id = request.POST.get("setores")
        setor = Setor.objects.get(id=setor_id)
        senha = request.POST.get("senha")

        user = CustomUser.objects.create(username=matricula, email=email,
        password=senha, first_name=nome, setor=setor)

        user.save()

        return render(request, 'home.html')