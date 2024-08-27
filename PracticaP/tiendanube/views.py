from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# Create your views here.

def home(request):  
    return render(request, 'home.html')

def signup(request):

    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        if request.POST['password'] == request.POST['confirm-password']:
            #registeer user
            try:
                User = User.objects.create_user(username=request.POST['nombre'], 
                                                password=request.POST['password'])
                User.save()
                return HttpResponse('usuario creado')
            except:
                return HttpResponse('user existente')
            
        return HttpResponse ('error contraseñas distintas')

