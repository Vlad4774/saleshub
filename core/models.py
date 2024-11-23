from django.db import models
from django.core.exceptions import ObjectDoesNotExist

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    
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
