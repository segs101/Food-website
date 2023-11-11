from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
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

def register(request):
    if request.method == 'POST':
        # check if user email already exist and redirect them to login page
        try:
            existing_user = get_object_or_404(User, email=request.POST.get('email'))
            if existing_user:
                messages.info(request, 'This email already exists, sign in instead.')
                return redirect('home')
        # process the register form and save it 
        except:
            form = MyUserCreationForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.username = user.username.lower()
                user.save()
                login(request, user)
                messages.success(request, f'Congratulations {user.full_name}, your account is created successfully.')
                return redirect('home')
            else:
                messages.error(request, form.errors)
    context = {
        "year": year,  # Make sure 'year' and 'category' are defined somewhere
        "category": category,
    }
    return render(request, 'signup.html', context)
   
  
def loginPage(request):
    # return user to home page if user is signed in
    if request.user.is_authenticated:
        return redirect('home')
    
    # process user login
    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')
        
        # check if user does not exist
        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, 'User does not exist   sign up instead')
            return redirect("signup")
        
    
        user = authenticate(request, email=email, password=password)

        if user:
            login(request, user)
            messages.success(request, 'Welcome back 🎉🎉')
            return redirect('home')
        else:
            messages.error(request, 'Username or password does not exit 😔😔')
            
    context = {
        "year": year,  # Make sure 'year' and 'category' are defined somewhere
        "category": category,
    }
    return render(request, 'signin.html', context)   


def logoutUser(request):
    logout(request)
    messages.success(request, "sign out successfully, come back soon we'll be waiting 😉😉")
    return redirect('login')

@login_required(login_url='login')
def book_table(request):
    context = {
        "year":year,
        "category": category,
    }
    return render(request, 'book-table.html', context)

