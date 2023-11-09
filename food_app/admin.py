from django.contrib import admin
from . models import *
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('food_name',)}
    list_display = ['id', 'food_name',  'slug']
    
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('product_name',)}
    list_display = ['product_name', 'pics', 'price', 'description', 'slug']  
    
    
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
