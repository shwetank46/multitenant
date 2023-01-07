from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegistrationForm
from .models import User
from django.contrib.auth import logout


def index(request):
    if request.user.is_authenticated:
        # Show the dashboard page
        return render(request, 'index.html')
    else:
        # Redirect the user to the login page
        return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                # Invalid login
                return redirect('/')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            password_confirm = form.cleaned_data['password_confirm']
            if password == password_confirm:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
            else:
                # Passwords do not match
                pass
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')