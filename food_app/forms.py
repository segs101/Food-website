from django import forms
from . models import *
from django.contrib.auth.forms import UserCreationForm
    
class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['full_name', 'email', 'password1', 'password2', 'address']    

class ContactForm(forms.ModelForm):
    class Meta:
        model = Home_Contact
        fields = "__all__"