from django.db import IntegrityError
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .forms import UserRegisterForm
from users.models import User
# Create your views here.

def User_Register(request):
    if request.method == 'GET':
        return render(request, 'registro_user.html',{
            'form' : UserRegisterForm()
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'], email=request.POST['email'], celular_cli=request.POST['celular_cli'], Nit_cli=request.POST['Nit_cli'])
                user.save()
                login(request, user)
                return render(request, 'registro_user.html', {
                        'form': UserRegisterForm(),
                        'error': 'registrado correctamente'
                    })  
            except IntegrityError:
                    return render(request, 'registro_user.html', {
                        'form': UserRegisterForm(),
                        'error': 'usurario ya existe'
                    })   
        return render(request, 'registro_user.html',{
            'form': UserRegisterForm(),
            'error': 'contrasena no coinciden'
            }) 

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('Inicio')  # Cambia 'home' por el nombre de tu vista de inicio
            else:
                error_message = "Credenciales inválidas. Por favor, inténtelo de nuevo."
                return render(request, 'login.html', {'form': form, 'error_message': error_message})
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('Inicio')