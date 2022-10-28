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
        setor = request.POST.get("setores")
        senha = request.POST.get("senha")


        user = CustomUser.objects.create_user(username=matricula, email=email,
        password=senha, first_name=nome)
        
        

        user.save()

        return render(request, 'home.html')