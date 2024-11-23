from django.contrib import admin
from .models import Product, Volume, Pricing, Cost

admin.site.register(Product)
admin.site.register(Volume)
admin.site.register(Pricing)
admin.site.register(Cost)
