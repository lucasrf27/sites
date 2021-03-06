from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)
from django.urls import reverse


def login_view (request):
    next = request.GET.get('next')
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('../../services/home')

    context = {
        'form': form,
    }
    return render(request, "login.html", context)

def register_view(request):
    next = request.GET.get('next')
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect('../../services/parceiro/add')

    context = {
        'form': form,
    }
    return render(request, "signup.html", context)

def logout_view(request):
    logout(request)
    return redirect ('../login')

