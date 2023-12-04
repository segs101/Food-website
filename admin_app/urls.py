from . views import *
from django.urls import path
from . import views

urlpatterns = [
    path("category", views.add_category, name="category"),
    path("delete_category/<str:id>", views.delete_category, name="delete_category"),
    path("category_update/<str:id>", views.category_update, name="category_update"),
    path("product", views.add_product, name="product"),
    path("update_product/<str:id>", views.update_product, name="update_product"),
]