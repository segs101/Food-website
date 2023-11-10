from django import forms
from . models import *
    
class ContactForm(forms.ModelForm):
    class Meta:
        model = Home_Contact
        fields = "__all__"