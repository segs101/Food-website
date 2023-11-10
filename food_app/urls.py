from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("product/<str:slug>", views.product, name='product'),
    path("book-table", views.book_table, name='book_table'),
]