from django.shortcuts import render
from .models import Produto
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


class HomeView(ListView):
    model = Produto
    template_name = 'produtos.html'
    list = Produto.objects.all()

    def get_queryset(self):
        return Produto.objects.all()


class addProduto(CreateView):
    model = Produto
    template_name = 'produto_form.html'
    fields = ['nome', 'preco', 'foto', 'year_in_school']
    success_url = '/produtos/'
