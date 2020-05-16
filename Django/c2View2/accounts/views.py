from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, get_user_model
from .forms import LoginForm, RegisterForm


def login_view(request):
    next = request.GET.get('next')
    form = LoginForm(request.POST or None)
    # se estiver escrito certo#
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        # autenticando o usuario#
        user = authenticate(username=username, password=password)
        # se estiver tudo certo (autendicado) chamar a função login#
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/c2vconfig/MP4')

    context = {
        'form2': form,
    }
    return render(request, "base.html", context)


def register_view(request):
    next = request.GET.get('next')
    form = RegisterForm(request.POST or None)
    # se estiver escrito certo#
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect('/c2vconfig/MP4')

    context = {
        'form': form,
    }
    return render(request, "register.html", context)


def logout_view(request):
    logout(request)
    return redirect('/c2vconfig/MP4')
