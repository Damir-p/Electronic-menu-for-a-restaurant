from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        # получение данных из POST-запроса
        name = request.POST['name']
        number = request.POST['number']
        password = request.POST['password']

        # создание нового пользователя
        user = User.objects.create_user(username=name, email=number, password=password)

        # сохранение пользователя в базе данных
        user.save()

        # вывод сообщения об успешной регистрации
        messages.success(request, 'You have successfully registered!')

        # перенаправление на страницу входа
        return redirect('login')

    return render(request, 'register.html')
