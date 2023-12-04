from django import forms
from . models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import PasswordResetForm
    
class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['full_name', 'email', 'password1', 'password2', 'address']    

class ContactForm(forms.ModelForm):
    class Meta:
        model = Home_Contact
        fields = "__all__"
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [ 'full_name',  'email', 'address']
        

class PasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(PasswordResetForm, self).__init__(*args, **kwargs)
        

class TableForm(forms.ModelForm):
    class Meta:
        model = Book_Table
        exclude = ['user']
        fields = "__all__"
        
