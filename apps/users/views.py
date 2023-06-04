from apps.users.forms import UserForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def SingUpUser(request):
    messages.error(request, 'Спасибо, что выбрали нас!')
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            if form.cleaned_data['password'] == request.POST.get("password2"):
                user.set_password(form.cleaned_data['password'])
                user.save()
                messages.success(request, 'Ваша учетная запись успешно создана!')
                return redirect("menu_list")
            else:
                messages.error(request, 'Пароли должны совпадать!')
    else:
        form = UserForm()
    return render(request, "signup.html", {"form": form, 'url': 'signup'})

def SingInUser(request):
    messages.error(request, 'Спасибо, что вы все еще с нами!')
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Вы успешно вошли в!')
            return redirect("menu_list") 
        else:
            messages.error(request, 'Неправильное имя пользователя или пароль!')

    return render(request, "login.html", {'url': 'login'})

def logoutUser(request):
    logout(request)
    messages.success(request, 'Вы успешно вышли из своей учетной записи!')
    return redirect("menu_list") 
