from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)
from .forms import UserLoginForm, UserRegisterForm
from django.contrib.auth.decorators import login_required
from products.models import Produto
from django.urls import reverse_lazy, reverse


def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/pruducts/home')

    context = {
        'form': form,
    }
    return render(request, "login.html", context)

@login_required
def register_view(request):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect('products/home')

    context = {
        'form': form,
    }
    return render(request, "signup.html", context)

def logout_view(request):
    logout(request)
    return redirect('../login')

def login_view2(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        login(request, user)
        # Redirect to a success page.
        return  redirect('../home')
    else:
        # Return an 'invalid login' error message.
        messages.error(request, 'user s not valid')
        return redirect('login')
    return render(request, "amp/login.html", {'form': form})

