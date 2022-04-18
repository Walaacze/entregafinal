from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate

# Create your views here.

def index(request):
    return render(request, 'accounts/index.html', {})

def about (request):
    return render(request, 'accounts/about.html')

def login(request):

    login_form = AuthenticationForm
    return render(request, 'accounts/login.html', {'login_form': login_form})
