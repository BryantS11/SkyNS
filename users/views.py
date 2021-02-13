from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm

# Create your views here.


def register(request):
    if request.method == 'POST':
        ur_form = UserRegisterForm(request.POST) # Form data

        if ur_form.is_valid():
            user = ur_form.save()# Save User Account
            username = ur_form.cleaned_data.get('username') # Pull username
            messages.success(request, f'Account created for {username}!, You are now able to login') # Show success Message in Template
            return redirect('login') # Redirect to Login
    else:
        ur_form = UserRegisterForm() # Get Request
    #
    context = {'ur_form': ur_form} # Add form to context
    return render(request, 'users/register.html', context) # render request to template
