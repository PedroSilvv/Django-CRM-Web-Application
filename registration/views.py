import email
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import CustomUser

def registration(request):
    if request.method == "GET":
        return render(request, 'registration.html')
    else:
        nome = request.POST.get("nome")
        email = request.POST.get("email")    
        matricula = request.POST.get("matricula")
        setor = request.POST.get("setor")
        senha = request.POST.get("senha")
    
        user = User.objects.create_user(username=matricula, email=email, password=senha)
        user.save()
        return render(request, 'home.html')