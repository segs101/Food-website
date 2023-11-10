from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib import messages
from . forms import *
import datetime
from . models import *
# Create your views here.
today = datetime.date.today()
year = today.year
category = Category.objects.all()

def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        messages.success(request, 'Your message has been sent successfully')
        new = Home_Contact(name=name, email=email, message=message)
        new.save()
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

def book_table(request):
    context = {
        "year":year,
        "category": category,
    }
    return render(request, 'book-table.html', context)

