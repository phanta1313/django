from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username']

class SaveProdForm(ModelForm):
    class Meta:
        model = category
        fields = '__all__'

 
        
        