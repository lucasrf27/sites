from django.shortcuts import render
from .models import Produto, Categoria
from django.views.generic import ListView


def HomeView(request):
    qs = Produto.objects.all()
    context = {'qs': qs}
    return render(request, 'mosaic/index_mosaic.amp.html', context)


class categoryView(ListView):
    template_name = 'mosaic/categorias_mosaic.amp.html'
    Model = Categoria

    def get_queryset(self):
        return(self.Model.objects.all())
