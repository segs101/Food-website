from django.shortcuts import render
from django.shortcuts import get_object_or_404
import datetime
from . models import *
# Create your views here.
today = datetime.date.today()
year = today.year
category = Category.objects.all()

def index(request):
    context = {
        "year":year,
        "category": category,
    }
    return render(request, 'main.html', context)

def product(request, slug):
    foodbrand = get_object_or_404(Category, slug=slug)
    type_slug_value =  slug
    product = Product.objects.filter(type__slug=type_slug_value)
    print(product)
    context = {
        "year":year,
        "foodbrand":foodbrand,
        "category": category,
        "product": product,
    }
    return render(request, 'product.html', context)
