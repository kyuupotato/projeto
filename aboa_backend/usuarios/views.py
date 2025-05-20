from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect



def index(request):
    return render(request, 'index.html')

def cadastro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'cadastro.html', {'form': form})

def recomendacoes(request):
    return render(request, 'recomenda.html')

class CustomLoginView(LoginView):
    template_name = 'login.html'

def cadastro_estabelecimento(request):
    erro = None

    if request.method == 'POST':
        username = request.POST['username']
        senha1 = request.POST['password1']
        senha2 = request.POST['password2']

        if senha1 != senha2:
            erro = "As senhas não coincidem."
        elif User.objects.filter(username=username).exists():
            erro = "Este usuário já está cadastrado."
        else:
            User.objects.create_user(username=username, password=senha1)
            return redirect('login_restaurante')  # ou home_comercio

    return render(request, 'cadastro_restaurante.html', {'erro': erro})
class LoginRestauranteView(LoginView):
    template_name = 'login_restaurante.html'

@login_required
def home_comercio(request):
    return render(request, 'home_restaurante.html')

def logout_view(request):
    logout(request)
    return redirect('index')