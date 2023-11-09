from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("product/<str:slug>", views.product, name='product')
]