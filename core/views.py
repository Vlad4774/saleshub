from django.shortcuts import render
from .models import Product

def home(request):
    products = Product.objects.all()
    return render(request, 'core/home.html', {'products': products})

def get_started(request):
    return render(request, 'core/get_started.html')

def login(request):
    return render(request, 'core/login.html')