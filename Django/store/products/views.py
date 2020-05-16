from django.shortcuts import render, redirect
from .models import Produto, Imagem, Modelo, Banner, BannerImages
from .forms import ProdutoForm, ImagemForm, ModeloForm, BannerForm, BannerImagesForm
from django.forms import modelformset_factory
from django.views.generic import DeleteView, UpdateView, ListView
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



#FRONT#

def amp_home(request):
    for b in Banner.objects.filter(tipo='Inicial'):
        filter1 = b.banner_image.all()
    filter2 = Banner.objects.filter(tipo='Mini')
    context = {
        'filter1': filter1,
        'filter2': filter2,
    }
    return render(request, 'amp/home.amp.html', context)



def list_view(request):
    query = Produto.objects.all()
    context = {
        'query': query
    }
    return render(request, 'amp/AllList.amp.html', context)


def kids_list_view(request):
  #  m = Modelo.objects.filter(publico ='Crianca')
  #  query = Produto.objects.filter(model=m)
    query = []
    for p in Produto.objects.all():
        p2 = p.model.publico
        if p2 =='Crianca':
            query.append(p)


    context = {
        'query': query
    }
    return render(request, 'amp/KidsList.amp.html', context)


def adult_list_view(request):
  #  m = Modelo.objects.filter(publico ='Crianca')
  #  query = Produto.objects.filter(model=m)
    query = []
    for p in Produto.objects.all():
        p2 = p.model.publico
        if p2 =='Adulto':
            query.append(p)


    context = {
        'query': query
    }
    return render(request, 'amp/AdultList.amp.html', context)


def detail_view(request, id):
    query = Produto.objects.get(id=id)
    context = {
        'query': query
    }
    return render(request, 'detail.amp.html')




                     #BACK#

@login_required
def add_modelo(request):
    if request.method == 'POST':
        form = ModeloForm(request.POST)
        if form.is_valid():
            form.save()
        
    else:
        form = ModeloForm()
   
    context = {
        'form': form,
    }
    return render(request, 'modelo_add.html', context)

@login_required
def add_product(request):
    ImagemFormSet = modelformset_factory(Imagem, fields=('image',), extra=4)
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        formset = ImagemFormSet(request.POST or None, request.FILES)
        if form.is_valid() and formset.is_valid():
            product = form.save(commit=False)
            product.save()

            for f in formset:
                try:
                    photo = Imagem(product=product, image=f.cleaned_data['image'])
                    photo.save()

                except Exception as e:
                    break
            return redirect('/products/admin')
    else:
        form = ProdutoForm()
        formset = ImagemFormSet(queryset=Imagem.objects.none())
    context = {
        'form': form,
        'formset': formset,
    }
    return render(request, 'produto_add.html', context)


def add_banner(request):
    BannerImageFormSet = modelformset_factory(BannerImages, fields=('imagem',), extra=4)
    if request.method == 'POST':
        form = BannerForm(request.POST)
        form2 = BannerImageFormSet(request.POST, request.FILES)
        if form.is_valid() and form2.is_valid():
            banner = form.save(commit=False)
            banner.save()
            for f in form2:
                try:
                    photo = BannerImages(banner=banner, imagem=f.cleaned_data['imagem'])
                    photo.save()

                except Exception as e:
                    break
            return redirect('/products/admin')
    else:
        form = BannerForm()
        form2 = BannerImageFormSet(queryset=Imagem.objects.none())
    context = {
        'form': form,
        'form2': form2,
    }
    return render(request, 'banner_add.html', context)

class AdminView(LoginRequiredMixin, ListView):
    model = Produto
    template_name = 'admin.html'
    
    def get_queryset(self):
        return Produto.objects.all()


class UpdateProduct(LoginRequiredMixin, UpdateView):
    model = Produto
    template_name = 'produto_add.html'
    fields = ['model', 'nome', 'preco', 'mini_gallery']
    succes_url = 'products/'


class DeleteProduct(LoginRequiredMixin, DeleteView):
    model = Produto


    def get_success_url(self):
        return reverse('admin_product')


def test_view(request):
    t1 = 'ok'
    return render(request, 'test.html', {'t1': t1})