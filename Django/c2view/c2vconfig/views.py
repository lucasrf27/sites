from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView
from .models import MP4, Tutorial
from django.urls import reverse, reverse_lazy
from urllib import request
from accounts.views import login_view
from random import randint



def ampView(request):
    queryset = MP4.objects.all()
    return render(request, 'amp/MP4amp.html', {'queryset': queryset})


class HomeView(TemplateView):
    template_name = 'home.html'


class MP4View(ListView):
    model = MP4
    template_name = 'MP4.html'

    def get_queryset(self):
        return MP4.objects.all()


class MP4create(CreateView):
    template_name = 'MP4form.html'
    success_url = '/c2vconfig/MP4'
    model = MP4
    queryset = MP4.objects.all()
    fields = ['nome', 'url', 'preço', 'imagem', 'artista']


class MP4update(UpdateView):
    model = MP4
    fields = ['nome', 'url', 'preço', 'imagem', 'artista']
    queryset = MP4.objects.all()
    template_name = 'MP4form.html'


class MP4delete(DeleteView):
    model = MP4
    success_url = reverse_lazy('MP4')


class TutorialView(ListView):
    model = Tutorial
    template_name = 'tutorial.html'

    def get_queryset(self):
        return Tutorial.objects.all()


class Tutorialcreate(CreateView):
    model = Tutorial
    template_name = 'Tutorialform.html'
    fields = ['assunto', 'url', 'preview', 'data', 'code', 'idioma']
    success_url = '/c2vconfig/tutorial'


class TutorialUpdate(UpdateView):
    model = Tutorial
    template_name = 'Tutorialform.html'
    fields = ['assunto', 'url', 'preview', 'data', 'code', 'idioma']
    success_url = '/c2vconfig/tutorial'


class TutorialDelete(DeleteView):
    model = Tutorial
    success_url = reverse_lazy('Tutorial.html')


def tester(request):
    t1 = MP4.objects.get(id=10)
    return render(request, 'tester.html', {'t1': t1 })
