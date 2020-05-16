from django.shortcuts import render, redirect
from .models import Servicos, Parceiros, Imagens
from django.views.generic import UpdateView, DetailView, ListView
from .forms import ParceirosForm, ServicosForm, ImagensForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.context_processors import auth
from django.contrib.auth.models import User
from django.db import transaction
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.forms import modelformset_factory


def home_view(request):
    serv = Servicos.objects.all()
    context = {'serv': serv }
    return render (request, 'home.html', context)

@login_required
@transaction.atomic
def parceiros_create(request):
    if request.method == 'POST':
        form = ParceirosForm(request.POST)
        if form.is_valid():
            part = form.save(commit=False)
            part.user = request.user
            part.save()
            messages.success(request, ('Parceiro criado'))
            return redirect('../parceiro/detail/{0}'.format(part.id))
            #return redirect(reverse('parceiro_detail2', kwargs={'part': part.id}))
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        form = ParceirosForm(instance=request.user)
    context = {
        'form': form,
    }
    return render (request, 'parceiroform.html', context)




def parceirosview(request, pk=None):
    parc = get_object_or_404(Parceiros, id=pk)
    context = {
        'parc': parc,
        }
    return render(request, 'parceiro.html', context)

    def get_queryset(self):
     return super().get_queryset().filter(parceiro__user=self.request.user)

class ParceirosView(DetailView):
    model = Parceiros
    template_name = 'parceiro2.html'
    
    def get_queryset(self):
        return Parceiros.objects.all()

class ParceiroUpdate(UpdateView):
    model = Parceiros
    template_name = 'parceiroform.html'
    fields = ['nome', 'endereco', 'responsavel', 'tel']
    
    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class ServicoView(DetailView):
    model = Servicos



@login_required
def service_create(request):
    ImageFormSet = modelformset_factory(Imagens, fields=('imagem',), extra=4)
    if request.method == 'POST':
        form = ServicosForm(request.POST)
        formset = ImageFormSet(request.POST or None, request.FILES)
        if form.is_valid() and formset.is_valid():
            service = form.save(commit=False)
            service.parceiro = request.user.parceiros
            service.save()

            for f in formset:
                try:
                    photo = Imagens(servicos=service, imagem=f.cleaned_data['imagem'])
                    photo.save()

                except Exception as e:
                    break
            return redirect(reverse('parceiro_detail2', kwargs={'service': service.id}))
    else:
        form = ServicosForm()
        formset = ImageFormSet(queryset=Imagens.objects.none())
    context = {
        'form': form,
        'formset': formset,
    }
    return render(request, 'servicoform.html', context)


class ServicoUpdate(UpdateView):
    model = Servicos