from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate, logout
from django.contrib.auth.decorators import login_required 
from .models import Product

@login_required
def home(request):
    products = Product.objects.all()
    return render(request, 'core/home.html', {'products': products})

def get_started(request):
    if request.user.is_authenticated:
        logout(request)
    return render(request, 'core/get_started.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            return render(request, 'core/login.html', {'error': 'Invalid credentials'})
    return render(request, 'core/login.html')

def base(request):
    return render(request, 'core/base.html')