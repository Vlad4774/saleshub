from django import forms
from .models import Product, Category, Customer, Location

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'short_description', 'description', 'category', 'sold_to', 'location']

    short_description = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 5}))
