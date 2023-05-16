from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.template.loader import get_template
from django.core.mail import EmailMessage
from .models import *

# Create your views here.
def log_user_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        # If username or password is incorrect, authenticate function returns None
        if user is not None:
            login(request, user)        # Logging user in
            return redirect('home')     # Redirecting to home page
        else:
            messages.info(request, 'Invalid Info.')
            return redirect('login')        # Redirecting to login page so that correct information can be entered

    data = {
        'title' : 'Login - TheNewsPro',     # Title of Login Page
    }

    return render(request, 'Accounts/Login.html', data)

def sign_user_up(request):
    signup_success = False      # Using this boolean variable so that when sign up is complete, we can display a message using if condition

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        country = request.POST.get('country')

        # When both passwords are same
        if password == password2:
            # In case same username already exists
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username already exists.')
                return redirect('signup')       # Returing user to signup page so that it can enter other username
            else:
                # Creating default Django User
                user = User.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name, password=password)
                user.save()
                # For extra field, using UserAccount model
                user_account = UserAccount(user=user, user_country=country)
                user_account.save()
                
                signup_success = True   # As sign up is complete so this boolean variable helps us to display sign up completion message
        else:
            messages.info(request,'Both passwords are not same.')
            return redirect('signup')

    data  ={
        'title' : 'Signup - TheNewsPro',        # Title on sign up page
        'signup_success' : signup_success
    }

    return render(request, 'Accounts/Signup.html', data)

def log_user_out(request):
    logout(request)     # Logging user out
    return redirect('home')
