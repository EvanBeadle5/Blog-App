from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, BioUpdateForm
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
            messages.success(request, f'Account created! You are now able to login')
            
            #redirects from registration page to 'blog-home' in blog/urls
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form' :form})

@login_required
def profile_page(request):
    
    if request.method == 'POST':
        '''
            request.POST - posts the inputted data into the respective form
            request.FILES - handling for image data
            request.user - user info       request.user.profile - profile info
        '''
        update_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        bio_form = BioUpdateForm(request.POST, instance=request.user.profile)
        
        if update_form.is_valid() and profile_form.is_valid() and bio_form.is_valid():
            update_form.save()
            profile_form.save()
            bio_form.save()
            
            #display message confirming success
            messages.success(request, f'Profile updated!')
            
                #redirect here because of ' POST GET redirect pattern '
            return redirect('profile')
    else:
        update_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
        bio_form = BioUpdateForm(instance=request.user.profile)
        
    context = {
        'update_form' : update_form,
        'profile_form' : profile_form,
        'bio_form' : bio_form,
    }
    return render(request, 'users/profile.html', context)
