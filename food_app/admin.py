from django.contrib import admin
from . models import *
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('food_name',)}
    list_display = ['id', 'food_name',  'slug']
    
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('product_name',)}
    list_display = ['type','product_name', 'pics', 'price', 'description']  
    
class Home_ContactAdmin(admin.ModelAdmin):
    list_display = ['id','name','email', 'message','submit_date']
    
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','email', 'joined']
     
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Home_Contact, Home_ContactAdmin)
admin.site.register(User, UserAdmin)
