import email
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import CustomUser, Setor

def registration(request):
    if request.method == "GET":
        return render(request, 'registration.html', context={
            "setores" : Setor.objects.values('nome'),
            'setor' : Setor.objects
        })

    else:
        nome = request.POST.get("nome")
        email = request.POST.get("email")    
        matricula = request.POST.get("matricula")
        setor_input = request.POST.get("setor")
        senha = request.POST.get("senha")

        setor_add = Setor.objects.get(nome=setor_input)
        
        user = CustomUser.objects.create_user(username=matricula, email=email,
        password=senha, first_name=nome, setor=setor_add)

        user.save()

        return render(request, 'home.html')