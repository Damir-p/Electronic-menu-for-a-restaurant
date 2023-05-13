from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages


def login_view(request):
    return render(request, 'login.html')

def register_view(request):
    return render(request, 'register.html')

from django.shortcuts import render

def home(request):
    return render(request, 'base.html')

def guest_login(request):
    if request.method == 'POST':
        password = request.POST['password']

        user = authenticate(request, username='guest', password=password)

        if user is not None:
            login(request, user)

            messages.success(request, 'You have logged in as a guest!')

            return redirect('profile')
        else:
            messages.error(request, 'Invalid password.')

    return render(request, 'guest_login.html')
