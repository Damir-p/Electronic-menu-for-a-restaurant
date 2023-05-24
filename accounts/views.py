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
        # получение данных из POST-запроса
        password = request.POST['password']

        # аутентификация гостевого пользователя
        user = authenticate(request, username='guest', password=password)

        if user is not None:
            # вход гостя в систему
            login(request, user)

            # вывод сообщения об успешном входе
            messages.success(request, 'You have logged in as a guest!')

            # определение URL, на который нужно перенаправить гостя
            next_url = request.GET.get('next', '/')
            return redirect(next_url)
        else:
            # вывод сообщения об ошибке аутентификации
            messages.error(request, 'Invalid password.')

    return render(request, 'guest_login.html')

