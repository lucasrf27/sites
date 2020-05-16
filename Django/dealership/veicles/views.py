from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View, CreateView, TemplateView, UpdateView
from .models import Veiculos, Imagens, Componentes
from .forms import VeicleForm, ImageForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from . import models
from django.forms import modelformset_factory
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required


def amp_home(request):
    filter1 = Veiculos.objects.filter(first_gallery=True)
    filter2 = Veiculos.objects.filter(mini_gallery=True)
    context = {
        'filter1': filter1,
        'filter2': filter2,
    }
    return render(request, 'amp/home.amp.html', context)


class CategoryView(ListView):
    model = Veiculos
    template_name = 'category.html'

    def get(self, request):
        queryset = self.model.objects.all()
        return render(request, self.template_name, {'queryset': queryset})


class DetailView(DetailView):
    model = Veiculos
    template_name = 'detail.html'
    
    

@login_required
def veicle_create2(request):
    ImageFormSet = modelformset_factory(Imagens, fields=('imagem',), extra=4)
    if request.method == 'POST':
        form = VeicleForm(request.POST)
        formset = ImageFormSet(request.POST or None, request.FILES)
        if form.is_valid() and formset.is_valid():
            veicle = form.save(commit=False)
            veicle.save()

            for f in formset:
                try:
                    photo = Imagens(veicle=veicle, imagem=f.cleaned_data['imagem'])
                    photo.save()

                except Exception as e:
                    break
            return redirect('category2')
    else:
        form = VeicleForm()
        formset = ImageFormSet(queryset=Imagens.objects.none())
    context = {
        'form': form,
        'formset': formset,
    }
    return render(request, 'veiclesform3.html', context)


def test_view(request):
    queryset = Veiculos.objects.all()
    filter1 = Veiculos.objects.filter(first_gallery=True)
    filter2 = Veiculos.objects.filter(mini_gallery=True)
    context = {
        'filter1': filter1,
        'filter2': filter2,
        'queryset': queryset
    }
    return render(request, 'test.html', context)


class VeicleUpdate(UpdateView):
    model = Veiculos
    template_name = "veiclesform3.html"
    fields = ['modelo','potencia','cor','preco','ano','category', 'first_gallery', 'mini_gallery']


def amp_detail(request):
    queryset = Veiculos.objects.all()
    return render(request, 'amp/detail.amp.html', {'queryset': queryset})

class amp_detail(DetailView):
    model = Veiculos
    template_name = 'amp/detail.amp.html'


def amp_category(request):
    queryset = Veiculos.objects.all()
    return render(request, 'amp/category.amp.html', {'veiculos': queryset})


###TESTS#####

def amp_category2(request):
    queryset = Veiculos.objects.all()
    return render(request,'amp/category2.amp.html', {'veiculos': queryset})

def amp_test(request):
    filter1 = Veiculos.objects.filter(first_gallery=True)
    filter2 = Veiculos.objects.filter(mini_gallery=True)
    context = {
        'filter1': filter1,
        'filter2': filter2,
    }
    return render(request, 'amp/test.amp.html', context)

def amp_test2(request):
    queryset = Veiculos.objects.all()
    photos = Veiculos.images
    return render(request, 'amp/test2.amp.html', {'queryset': queryset}, {'phtos': photos})
    