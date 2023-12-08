from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.conf import settings
from . forms import *
from . models import *
from random import randint
import uuid
import requests
import os


# Create your views here.
api_key = settings.PAYSTACK_TEST_SECRETE_KEY
def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        messages.success(request, 'Your message has been sent successfully')
        new = Home_Contact(name=name, email=email, message=message)
        new.save()
    context = {}
    print(f"DEBUG: MEDIA_ROOT: {settings.MEDIA_ROOT}")
    print(f"DEBUG: MEDIA_URL: {settings.MEDIA_URL}")
    return render(request, 'main.html', context)

def product(request, slug):
    foodbrand = get_object_or_404(Category, slug=slug)
    type_slug_value =  slug
    product = Product.objects.filter(type__slug=type_slug_value)
    context = {
        "foodbrand":foodbrand,
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
                user.email = user.email.lower()
                user.save()
                #create cart for every user
                Cart.objects.create(user=user)
                login(request, user)
                messages.success(request, f'Congratulations {user.full_name}, your account is created successfully.')
                return redirect('login')
            else:
                messages.error(request, form.errors)
    context = {
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
        
        if user and user.is_superuser:
            try:
                Cart.objects.get(user=user)
            except Cart.DoesNotExist:
                Cart.objects.create(user=user)
            login(request, user)
            return redirect('profile')
        elif user:
            login(request, user)
            messages.success(request, f'Welcome back {request.user.full_name} 🎉🎉')
            return redirect('home')
        else:
            messages.error(request, 'Username or password does not exit 😔😔')
            
    context = {
    }
    return render(request, 'signin.html', context)   

def logoutUser(request):
    logout(request)
    messages.success(request, "sign out successfully, come back soon we'll be waiting 😉😉")
    return redirect('login')

@login_required(login_url='login')
def book_table(request):
    form = TableForm()
    if request.method == "POST":
        form = TableForm(request.POST)
        print(request.POST)
        if form.is_valid():
            table_instance = form.save(commit=False)
            table_instance.user = request.user# Assign the user to the table instance
            # print(table_instance)
            table_instance.save()
            messages.success(request, "Table booked successfully")
        else:
            print(form.errors)
            messages.error(request, "error")
    context = {
        "form":form,
    }
    return render(request, 'book-table.html', context)

@login_required(login_url='login')
def cart(request):
    global api_key
    cart = request.user.cart
    cart_items = CartItem.objects.filter(cart=cart)
    amount = sum(int(product.amount)for product in cart_items)
    context = {
        "cart_item": cart_items,
        "amount": amount,
    }
    return render(request, 'cart.html', context)


@login_required(login_url='login')
def add_to_cart(request, product_id):
    product = Product.objects.get(pk=product_id)
    cart,created = Cart.objects.get_or_create(user=request.user)
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)
    cart_item.amount = cart_item.quantity * cart_item.product.price
    if not item_created:
        cart_item.quantity += 1
        cart_item.amount = cart_item.quantity * cart_item.product.price
    cart_item.save()
    messages.success(request, "successfully added an item to your cart")
    return redirect(request.META.get('HTTP_REFERER')) #redirect to the previous url  

@login_required(login_url='login')
def remove_from_cart(request, product_id):
    product = Product.objects.get(pk=product_id)
    cart = Cart.objects.get(user=request.user)
    try:
        cart_item = cart.cartitem_set.get(product=product)
        if cart_item.quantity >= 1:
            cart_item.delete()
    except CartItem.DoesNotExist:
        pass
    return redirect('cart')

@login_required(login_url='login')
def increase_cart_item(request, product_id):
    product = Product.objects.get(pk=product_id)
    cart = request.user.cart
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    cart_item.quantity += 1
    cart_item.amount = cart_item.quantity * cart_item.product.price
    cart_item.save()

    return redirect('cart')

@login_required(login_url='login')
def decrease_cart_item(request, product_id):
    product = Product.objects.get(pk=product_id)
    cart = request.user.cart
    cart_item = cart.cartitem_set.get(product=product)

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.amount = cart_item.quantity * cart_item.product.price
        cart_item.save()
    else:
        cart_item.delete()

    return redirect('cart')

@login_required(login_url='login')
def update_cart_item(request, product_id):
    if request.method == 'POST':
        product = Product.objects.get(pk=product_id)
        cart = request.user.cart
        cart_item = cart.cartitem_set.get(product=product)
        if cart_item.quantity > 1:
            cart_item.quantity = request.POST.get('num')
            cart_item.amount = cart_item.quantity * cart_item.product.price
            cart_item.save()
        return redirect('cart')
    
@login_required(login_url='login')
def check_out(request):
    cart = request.user.cart
    cart_items = CartItem.objects.filter(cart=cart)
    amount = sum(int(product.amount)for product in cart_items)
    discount_percentage = 20
    delivery_fee = randint(1000, 2000)
    is_discount = False
    discount_price = 0
    # (part / whole) * 100
    if request.method == "POST":
        discount = request.POST.get('discount').lower()
        if discount == "newuicool":
            is_discount = True
            messages.success(request, "coupon added successfully")
        else:
             messages.error(request, "invalid coupon")
            
    if is_discount:
        discoun_price = (discount_percentage / 100) * amount
        discount_price = round(discoun_price, 2)
        
    total_amount = round(amount + delivery_fee - discount_price, 2)
    # Store total_amount in the session
    request.session['total_amount'] = total_amount
    print(request.session.get('total_amount', 0.0))
    context = {
        "cart_item": cart_items,
        "amount": amount,
        "total_amount": total_amount,
        "discount": discount_price,
        "delivery_fee": delivery_fee,
    }
    return render(request, 'checkout.html', context)

def pay(request):
    global api_key
    print(os.environ.get('paystack_public_key'))
    curl = settings.PAYSTACK_INITIALIZE_PAYMENT_URL
    if request.method == 'POST':
        user = request.user
        cart = user.cart
        cart_items = CartItem.objects.filter(cart=cart)
        # Retrieve total_amount from the session
        total_amount = request.session.get('total_amount')
        try:
            order = Order.objects.create(user=user, total_amount=total_amount)
            # set the payment in the current session
            request.session['order_id'] = order.id
            for item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    quantity=item.quantity,
                    item_total=int(item.quantity*item.product.price),
                )
            ref = str(uuid.uuid4())
            request.session['ref'] = ref
            headers = {'Authorization': f'Bearer {api_key}'}
            data = {
                'reference':ref,
                'amount':f"{total_amount:.2f}",
                'email':user.email,
                'callback_url':'http://127.0.0.1:8000/payment_success',
                'currency':'NGN'
                }
            # making a post request 
            try:
                r = requests.post(curl, headers=headers, json=data) 
            except Exception:
                messages.error(request, 'network busy, try again')
            else:
                transback = r.json()
                if transback["status"] == True :
                    rdurl = transback['data']['authorization_url']
                    cart_items.delete()
                    return redirect(rdurl)
            
            # delete total price from session
            if 'total_amount' in request.session:
                del request.session['total_amount']   
        except:
            pass
        return redirect('checkout')
             
def payment_success(request):
    user = request.user
    cart = user.cart
    cart_items = CartItem.objects.filter(cart=cart)
    # retrieve the payment_id we'd set in the django session earlier
    order_id = request.session.get('order_id', None) #new
    # using the payment_id, get the database object
    payment = get_object_or_404(Order, id=order_id) #new

    # retrieve the ref we'd set in the django session earlier
    ref = request.session.get('ref', None) #new
    # verify transaction endpoint
    url = 'https://api.paystack.co/transaction/verify/{}'.format(ref)#new

    # set auth headers
    headers = {"authorization": f"Bearer {api_key}"}#new
    r = requests.get(url, headers=headers)#new
    res = r.json() #new
    res = res["data"]

    # verify status before setting payment_ref
    if res['status'] == "success":  # new
        # update payment payment reference
        cart_items.delete()
        payment.payment_status = True 
        payment.payment_id = res["id"]#new
        payment.save()#new
        messages.success(request, "payment successful")
        # delete order_id price from session
        if 'order_id' in request.session:
            del request.session['order_id']   

    return redirect('cart')

@login_required
def profile(request):
    return render(request, 'profile/profile.html', {"user": request.user})

@login_required
def orders(request):
    user = request.user
    order =  Order.objects.filter(user=user)
    order_item = None
    if user.is_superuser:
        order_item = OrderItem.objects.all().order_by('-order_id')
    else:
        order_item = OrderItem.objects.filter(order__in=order).order_by('-order__created_at')
    context = {
        "user": user,
        "order_item": order_item,
    }
    print(order_item)
    return render(request, 'profile/orders.html', context)

@login_required
def reservation(request):
    user = request.user
    if user.is_superuser:
        book = Book_Table.objects.all().order_by('-id')
    else:
        book = Book_Table.objects.filter(user=user).order_by('-id')
    return render(request, 'profile/reservation.html', {"book": book})

@login_required
def password_change(request):
    user = request.user
    if request.method == 'POST':
        form = PasswordChangeForm(user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your password has been changed")
            return redirect('login')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)      
    form = PasswordChangeForm(user)
    return render(request, 'password_reset/password_update.html', {'form': form})