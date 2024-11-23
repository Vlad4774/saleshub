from django import template

register = template.Library()

@register.filter
def is_product_page(value):
    return value.startswith('/product/')

@register.filter
def get_volume(data, year):
    
    if data and year in data:
        return data[year]
    return None