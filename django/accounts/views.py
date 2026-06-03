from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, logout


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created successfully for {username}! You can now log in.')
            return redirect('signup')  # Redirect to your signup URL name later
    else:
        form = UserCreationForm()
    
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Retrieve the validated user object
            user = form.get_user()
            # Log the user into the session
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('home')  # Redirect to a home/dashboard page after login
    else:
        form = AuthenticationForm()
        
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('login')

def home_view(request):
    return render(request, 'accounts/home.html')