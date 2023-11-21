from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("product/<str:slug>", views.product, name='product'),
    path("book-table", views.book_table, name='book_table'),
    path("signup", views.register, name='signup'),
    path('logout', views.logoutUser, name="logout"),
    path('sign-in', views.loginPage, name="login"),
    path('profile', views.profile, name="profile"),
    path('cart', views.cart, name="cart"),
    path('add-to-cart/<str:product_id>', views.add_to_cart, name="add-to-cart"),
    path('remove-from-cart/<str:product_id>', views.remove_from_cart, name="remove-from-cart"),
    path('increase-cart-item/<str:product_id>', views.increase_cart_item, name="increase-cart-item"),
    path('decrease-cart-item/<str:product_id>', views.decrease_cart_item, name="decrease-cart-item"),
    path('update-cart-item/<str:product_id>', views.update_cart_item, name="update-cart-item"),
    path('checkout', views.check_out, name="checkout"),
    path('pay', views.pay, name="pay"),
    path('payment_success', views.payment_success, name="payment_success"),
]