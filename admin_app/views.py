from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from .forms import *
# Create your views here.


def is_admin_or_superuser(user):
    return user.is_authenticated and (user.is_staff or user.is_superuser)

@user_passes_test(is_admin_or_superuser)
def add_category(request):
    if request.method == "POST":
        form =CategoryForm(request.POST,  request.FILES)
        if form.is_valid():
            form.save()
            messages.success(
                request, f"successfully added {request.POST.get('food_name')} to category")
        else:
            print(form.errors)
    form = CategoryForm()
    return render(request, 'profile/category.html', {'form': form})


@user_passes_test(is_admin_or_superuser)
def delete_category(request, id):
    # dictionary for initial data with
    # field names as keys

    # fetch the object related to passed id
    obj = get_object_or_404(Category, pk=id)
    if request.method == "POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # redirect to the previous url
        return redirect(request.META.get('HTTP_REFERER'))


@user_passes_test(is_admin_or_superuser)
def category_update(request, id):
    category = get_object_or_404(Category, id=id)
    if request.method == "POST":
        form = CategoryForm(request.POST or None, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, f"successfully updated {request.POST.get('food_name')}category")
            return redirect('category')
    form = CategoryForm(instance=category)
    return render(request, 'profile/category.html', {'form': form})
        

@user_passes_test(is_admin_or_superuser)
def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST,  request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f"successfully added {request.POST.get('product_name')} to product")
        else:
           messages.errors(request, f"{form.errors}") 
            
    form = ProductForm()
    return render(request, 'profile/product.html', {'form': form})


@user_passes_test(is_admin_or_superuser)
def update_product(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == "POST":
        form = ProductForm(request.POST or None, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f"successfully updated {request.POST.get('product_name')} product")
            return redirect('product')
    form = ProductForm(instance=product)
    return render(request, 'profile/product.html', {'form': form})