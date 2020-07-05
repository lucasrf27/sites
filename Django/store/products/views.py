from django.shortcuts import render, redirect
from .models import Produto, Imagem, Modelo, Banner, BannerImages
from .forms import ProdutoForm, ImagemForm, ModeloForm, BannerForm, BannerImagesForm, ContactForm
from django.forms import modelformset_factory
from django.views.generic import DeleteView, UpdateView, ListView
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from cart.models import Pedido, Item
from accounts.decorators import allowed_users 
from django.db.models import Q


#FRONT#
def amp_home(request):
    for b in Banner.objects.filter(tipo='Inicial'):
        filter1 = b.banner_image.all()
    filter2 = Banner.objects.filter(tipo='Mini')
    context = {
        'filter1': filter1,
        'filter2': filter2,
        }
    if request.user_agent.is_mobile:
        return render(request, 'amp/home.amp.html', context)
    elif request.user_agent.is_pc:
        return render (request, 'desktop/home.amp.html', context)
    else:
        return render (request, 'amp/home.amp.html', context)



def list_view(request):
    model_query = request.GET.get('model_query', '')
    price_query = request.GET.get('price_query', '')
    size_query = request.GET.get('size_query', '')
    sex_query = request.GET.get('sex_query', '')

    if model_query or price_query or size_query:
        query = Produto.objects.filter(Q(model__modelo__icontains=model_query),
            Q(preco__lte=price_query),
            Q(model__tamanho__icontains=size_query),
            Q(model__sexo__icontains=sex_query))
    
    
    else:
        query = Produto.objects.all()

    if not request.user.is_anonymous:
        pedido = Pedido.objects.get_or_create(owner=request.user, is_ordered=False)
        context = {
            'pedido': pedido,
            'query': query
        }
    else:
        context = {
            'query': query
        }
    if request.user_agent.is_mobile:
        return render(request, 'amp/AllList.amp.html', context)
    elif request.user_agent.is_pc:
        return render (request, 'desktop/AllList.amp.html', context)
    else:
        return render (request, 'amp/AllList.amp.html', context)

def kids_list_view(request):
    model_query = request.GET.get('model_query', '')
    price_query = request.GET.get('price_query', '')
    size_query = request.GET.get('size_query', '')
    sex_query = request.GET.get('sex_query', '')
    age_query = request.GET.get('age_query', '')


    if model_query or price_query or size_query or sex_query or age_query:
        query = Produto.objects.filter(Q(model__publico='Crianca'), Q(model__modelo__icontains=model_query),
            Q(preco__lte=price_query),
            Q(model__tamanho__icontains=size_query),
            Q(model__sexo__icontains=sex_query),
            Q(model__idade_min__gte=age_query))
    
    
    else:
        query = Produto.objects.filter(Q(model__publico='Crianca'))

    if not request.user.is_anonymous:
        pedido = Pedido.objects.get_or_create(owner=request.user, is_ordered=False)
        context = {
            'pedido': pedido,
            'query': query
        }
    else:
        context = {
            'query': query
        }
    if request.user_agent.is_mobile:
        return render(request, 'amp/KidsList.amp.html', context)
    elif request.user_agent.is_pc:
        return render (request, 'desktop/KidsList.amp.html', context)
    else:
        return render (request, 'amp/KidsList.amp.html', context)

def adult_list_view(request):
    model_query = request.GET.get('model_query', '')
    price_query = request.GET.get('price_query', '')
    size_query = request.GET.get('size_query', '')
    sex_query = request.GET.get('sex_query', '')

    if model_query or price_query or size_query:
        query = Produto.objects.filter(Q(model__publico='Adulto'), Q(model__modelo__icontains=model_query),
            Q(preco__lte=price_query),
            Q(model__tamanho__icontains=size_query),
            Q(model__sexo__icontains=sex_query))
    
    
    else:
        query = Produto.objects.filter(Q(model__publico='Adulto'))

    if not request.user.is_anonymous:
        pedido = Pedido.objects.get_or_create(owner=request.user, is_ordered=False)
        context = {
            'pedido': pedido,
            'query': query
        }
    else:
        context = {
            'query': query
        }
    if request.user_agent.is_mobile:
        return render(request, 'amp/AdultList.amp.html', context)
    elif request.user_agent.is_pc:
        return render (request, 'desktop/AdultList.amp.html', context)
    else:
        return render (request, 'amp/AdultList.amp.html', context)

def detail_view(request, id):
    prod = get_object_or_404(Produto, pk=id)
    context = {
        'prod': prod,
    }
    if request.user_agent.is_mobile:
        return render(request, 'amp/detail.amp.html', context)
    elif request.user_agent.is_pc:
        return render (request, 'desktop/detail.amp.html', context)
    else:
        return render (request, 'desktop/detail.amp.html', context)

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_product')

    else:
        form = ContactForm()


    context = {'form': form}
    if request.user_agent.is_mobile:
        return render(request, 'amp/contact.amp.html', context)
    elif request.user_agent.is_pc:
        return render (request, 'desktop/contact.amp.html', context)
    else:
        return render (request, 'desktop/contact.amp.html', context)


def chat_view(request):
    if request.user_agent.is_mobile:
        return render(request, 'amp/chat.amp.html')
    elif request.user_agent.is_pc:
        return render (request, 'desktop/chat.amp.html')
    else:
        return render (request, 'desktop/chat.amp.html')



                     #BACK#
@login_required
@allowed_users(allowed_ones=['Admin', 'Vendedor'])
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
    return render(request, 'admin/modelo_add.html', context)

@login_required
@allowed_users(allowed_ones=['Admin', 'Vendedor'])
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
    return render(request, 'admin/produto_add.html', context)

@login_required
@allowed_users(allowed_ones=['Admin', 'Vendedor'])
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
    return render(request, 'admin/banner_add.html', context)

@allowed_users(allowed_ones=['Admin', 'Vendedor'])
def admin_view(request):
    query = Produto.objects.all()
    context = {
        'query': query,
    }
    return render (request, "admin/admin.html", context)

@allowed_users(allowed_ones=['Admin', 'Vendedor'])
def update_product(request, pk):
    ImagemFormSet = modelformset_factory(Imagem, fields=('image',), extra=4)
    if request.method == 'POST':
        prod = Produto.objects.get(id=pk) 
        form = ProdutoForm(request.POST, instance=prod)
        formset = ImagemFormSet(request.POST or None, request.FILES)
        if form.is_valid() and formset.is_valid():
            prod.save()
            pic = formset.save(commit=False)
            for p in pic:
                p.product = prod
                p.save()
            return redirect('/products/admin/')
    else:
        form = ProdutoForm()
        prod = Produto.objects.get(id=pk)
        formset = ImagemFormSet
    context = {
        'form': form,
        'prod': prod,
        'formset': formset,
    }
    return render (request, 'admin/produto_add.html', context)


@allowed_users(allowed_ones=['Admin'])
def delete_product(request):
    prod = Produto.objects.get(pk=id)
    prod.delete()
    return redirect('/products/admin')

@login_required
@allowed_users(allowed_ones=['Admin'])
def test_view(request):
    query1 = Produto.objects.all()
    context = {'query1': query1}
    if request.user_agent.is_mobile:
        return render(request, 'amp/test.amp.html', context)
    elif request.user_agent.is_pc:
        return render (request, 'desktop/test.amp.html', context)
    else:
        return render (request, 'test.html', context)