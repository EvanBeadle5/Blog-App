from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#modified userCreationForm - includes email requirement
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    
    class Meta:
        #desired model UserRegisterForm to interact with
        model = User
        fields = [
            'username', 
            'email', 
            'password1', 
            'password2',
        ]
