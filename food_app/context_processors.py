from . models import *
import datetime

def site_settings(request):
    today = datetime.date.today()
    year = today.year
    category = Category.objects.all()
    return {'category': category, 'year': year}

def order_item_count(request):
    if request.user.is_authenticated:
        cart = request.user.cart
        cart_items = CartItem.objects.filter(cart=cart)
        return {'order_item_count': cart_items.count()}
    return {'order_item_count': 0}