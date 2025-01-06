# views.py

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.urls import path

# views.py
def main(request):
    return render(request, 'main.html')
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        phone_number = request.POST['phone_number']

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')

        # Create the user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.phone_number = phone_number  # Add phone number to user instance
        user.save()

        messages.success(request, "Account created successfully. You can now login.")
        return redirect('login')
    else:
        return render(request, 'signup.html')

def user_login(request):
    if request.method == 'POST':
        username_or_email = request.POST['username_or_email']
        password = request.POST['password']

        # Check if user exists
        if '@' in username_or_email:
            user = authenticate(request, email=username_or_email, password=password)
        else:
            user = authenticate(request, username=username_or_email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful.")
            return redirect('home:wwe')  # Redirect to home page after successful login
        else:
            messages.error(request, "Invalid username/email or password.")
            return redirect('login')
    else:
        return render(request, 'login.html')
