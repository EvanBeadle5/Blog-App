from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

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

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    
    class Meta:
        #Fields to update username and email
        model = User
        fields = [
            'username', 
            'email',
        ]
        
class BioUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic']
