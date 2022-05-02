from django import template
from kzsport.models import *

register = template.Library()

@register.simple_tag()
def get_cities():
    return City.objects.all()

@register.inclusion_tag('kzsport/list_foods.html')
def show_foods():
    foods = Food.objects.all()
    return {'foods' : foods}

