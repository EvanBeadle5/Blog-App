from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from .models import Profile
from django.contrib.auth.decorators import login_required

# Registration.
def register(request):
    #checks whether the user is trying to POST information
    if request.method == 'POST':
        
        #create form will supplied information
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            
            #save created user
            form.save()
            
            #display message confirming successful creation
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created! You are now able to login')
            
            #redirects from registration page to 'blog-home' in blog/urls
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form' :form})

@login_required
def profile_page(request):
    bio = Profile.bio
    return render(request, 'users/profile.html')
