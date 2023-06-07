from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from django.views import View
from .forms import UserForm


class SignUpUserView(View):
    def get(self, request):
        form = UserForm()
        return render(request, "signup.html", {"form": form})

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password'] == form.cleaned_data['confirm_password']:
                user = form.save(commit=True)
                user.set_password(form.cleaned_data['password'])
                user.save()
                messages.success(request, 'Ваша учетная запись успешно создана!')
                return redirect("menu_list")
            else:
                messages.error(request, 'Пароли должны совпадать!')
        return render(request, "signup.html", {"form": form})


class SignInUserView(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Вы успешно вошли в систему!')
            return redirect("menu_list") 
        else:
            messages.error(request, 'Неправильное имя пользователя или пароль!')
            return render(request, "login.html")


class LogoutUserView(View):
    def get(self, request):
        logout(request)
        messages.success(request, 'Вы успешно вышли из своей учетной записи!')
        return redirect("menu_list")
