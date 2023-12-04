from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("product/<str:slug>", views.product, name='product'),
    path("book-table", views.book_table, name='book_table'),
    path("signup", views.register, name='signup'),
    path('logout', views.logoutUser, name="logout"),
    path('sign-in', views.loginPage, name="login"),
    path('profile', views.profile, name="profile"),
    path('orders', views.orders, name="orders"),
    path('reservation', views.reservation, name="reservation"),
    path('password_change', views.password_change, name="password_change"),
    path('password_reset', auth_views.PasswordResetView.as_view(
        template_name='password_reset/password_reset_form.html',
        email_template_name='password_reset/password_reset_email.html',
        subject_template_name='password_reset/password_reset_subject.txt',
        success_url='password_reset_done'
    ), name='password_reset'),
    path('password_reset_done', auth_views.PasswordResetDoneView.as_view(
        template_name='password_reset/password_reset_done.html'
    ), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='password_reset/password_reset_confirm.html',
        success_url='password_reset_complete'
    ), name='password_reset_confirm'),
    path('password_reset_complete', auth_views.PasswordResetCompleteView.as_view(
        template_name='password_reset/password_reset_complete.html'
    ), name='password_reset_complete'),
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