from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login, authenticate, logout
from django.contrib.auth.decorators import login_required 
from .models import Product, Pricing, Volume, Cost
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.db import transaction
from .forms import ProductForm

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

def product_detail(request, id):
    product = Product.objects.get(id=id)

    volumes = Volume.objects.filter(product=product)
    volume_data = list(volumes.values('year', 'min_volume', 'expected_volume', 'max_volume'))
    prices = Pricing.objects.filter(product=product)
    prices_data = list(prices.values('year', 'base_price', 'packaging_price', 'transport_price', 'warehouse_price'))
    costs = Cost.objects.filter(product=product)
    costs_data = list(costs.values('year', 'base_cost', 'labor_cost', 'material_cost', 'overhead_cost'))
    return render(request, 'core/product.html', {
        'product': product,
        'volume_data': volume_data,
        'prices_data': prices_data,
        'costs_data': costs_data,
    })


@csrf_exempt
def save_product_changes(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            updated_data = data.get('updated_data', [])

            with transaction.atomic():
                for item in updated_data:
                    try:
                        volume_data = Volume.objects.get(id=item['id'])
                        volume_data.year = item['year']
                        volume_data.min_volume = item['min_volume']
                        volume_data.expected_volume = item['expected_volume']
                        volume_data.max_volume = item['max_volume']
                        volume_data.save()
                        print(f"Updating volume with ID {item['id']}")
                        print(f"New values: {item['year']}, {item['min_volume']}, {item['expected_volume']}, {item['max_volume']}")


                    except Volume.DoesNotExist:
                        # Log the ID of the missing volume for debugging purposes
                        print(f"Volume with ID {item['id']} not found")

            return JsonResponse({'success': True})

        except Exception as e:
            # Log the full exception for debugging purposes
            print(f"Error: {str(e)}")
            return JsonResponse({'success': False, 'error': str(e)})

    return JsonResponse({'success': False, 'error': 'Invalid request method'})

def create_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the product list page or wherever you want
    else:
        form = ProductForm()

    return render(request, 'core/create_product.html', {'form': form})

