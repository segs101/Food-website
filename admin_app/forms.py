from django import forms
from food_app.models import *


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        # exclude = ['slug']
        fields = "__all__"
        

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        # exclude = ['slug']
        fields = "__all__"
