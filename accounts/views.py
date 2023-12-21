from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserRegisterForm, UserLoginForm

def user_register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(cd["username"], cd["email"], cd["password"])
            user.first_name = cd["first_name"]
            user.last_name = cd["last_name"]
            user.save()
            messages.success(request, "ثبت نام با موفقیت انجام شد", 'success')
            return redirect("accounts:user_login")
    else:
        form = UserRegisterForm()
    return render(request, "accounts/register.html", {"form" : form})
        

def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd["username"], password = cd["password"])
            if user is not None:
                login(request, user)
                messages.success(request, "ورود به سایت با موفقیت انجام شد", 'success')
                return redirect("web:home")
            else:
                messages.error(request, "نام کاربری یا رمز عبور اشتباه است", 'danger')
                return redirect("accounts:user_login")
    else:
        form = UserLoginForm()
    return render(request, "accounts/login.html", {"form" : form})

def user_logout(request):
    logout(request)
    messages.success(request, "خارج شدن از سایت با موفقیت انجام شد", 'success')
    return redirect("web:home")