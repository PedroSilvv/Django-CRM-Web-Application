from django.shortcuts import render
from django.http import HttpResponse

#Request para login.html mandado para url /login
def login(request):
    return render(request, 'login.html')



