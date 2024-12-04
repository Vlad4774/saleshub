from django.db import models
from django.core.exceptions import ObjectDoesNotExist

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Location(models.Model):
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.city}, {self.country}"

class Product(models.Model):
    name = models.CharField(max_length=255)
    short_description = models.CharField(max_length=500)
    description = models.TextField() 
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    sold_to = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.name


class Volume(models.Model):
    product = models.ForeignKey(Product, related_name='volumes', on_delete=models.CASCADE)
    year = models.IntegerField()  
    min_volume = models.FloatField()
    expected_volume = models.FloatField()
    max_volume = models.FloatField()

class Pricing(models.Model):
    product = models.ForeignKey(Product, related_name='pricing', on_delete=models.CASCADE)
    year = models.IntegerField() 
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    packaging_price = models.DecimalField(max_digits=10, decimal_places=2)
    transport_price = models.DecimalField(max_digits=10, decimal_places=2)
    warehouse_price = models.DecimalField(max_digits=10, decimal_places=2)

class Cost(models.Model):
    product = models.ForeignKey(Product, related_name='costs', on_delete=models.CASCADE)
    year = models.IntegerField() 
    base_cost = models.DecimalField(max_digits=10, decimal_places=2)
    labor_cost = models.DecimalField(max_digits=10, decimal_places=2)
    material_cost = models.DecimalField(max_digits=10, decimal_places=2)
    overhead_cost = models.DecimalField(max_digits=10, decimal_places=2)
