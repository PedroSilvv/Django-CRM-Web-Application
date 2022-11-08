from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_crm, logout

#Request para login.html mandado para url /login
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    else:
        matricula = request.POST.get('matricula')
        senha = request.POST.get('senha')

        user = authenticate(username=matricula, password=senha)

        if user:
            login_crm(request, user)
            return render(request, 'home.html')
        
        else:
            return HttpResponse('Matricula ou Senha inexistentes em nosso sistema.')

"""
def logout(request):

    logout(request)

    return render(request, 'login.html')

"""