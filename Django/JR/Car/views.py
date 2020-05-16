from django.shortcuts import render
from django.shortcuts import render, redirect
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import ImageForm2, PostForm, ImageForm, VeicleForm
from .models import Images, Post, Veiculos, Imagens
from django.views.generic import View, TemplateView



class HomeView(TemplateView):
    template_name = 'home.html'
    model = Post

    def get_queryset(self):
        return Post.objects.all()


def addProduto(request):
    postForm = PostForm
    imageForm = ImageForm

    def get(request, self):
        postForm = PostForm
        imageForm = ImageForm
        return render(request, 'index.html', {'postForm': postForm, 'imageForm': imageForm})

    def post(request, self):

        ImageFormSet = modelformset_factory(Images,
                                            fields=('image',), extra=3)
        # 'extra' means the number of photos that you can upload   ^
        if request.method == 'POST':

            postForm = PostForm(request.POST)
            formset = ImageFormSet(request.POST, request.FILES,
                                   queryset=Images.objects.none())

            if postForm.is_valid() and formset.is_valid():
                post_form = postForm.save(commit=False)
                post_form.save()
                formset.save()

            else:
                print(postForm.errors, formset.errors)
        else:
            postForm = PostForm()
            formset = ImageFormSet(queryset=Images.objects.none())
        return render(request, 'index.html',
                      {'postForm': postForm, 'formset': formset})

    return render(request, 'index.html', {'postForm': postForm, 'imageForm': imageForm})


def addProduto2(request):
    ImageFormSet = modelformset_factory(Images, fields=('image',), extra=4)
    if request.method == 'POST':
        form = PostForm(request.POST)
        formset = ImageFormSet(request.POST or None, request.FILES or None)
        if form.is_valid() and formset.is_valid():
            post = form.save(commit=False)
            post.save()

            for f in formset:
                try:
                    photo = Images(post=post, image=f.cleaned_data['image'])
                    photo.save()
                except Exception as e:
                    break

    else:
        form = PostForm()
        formset = ImageFormSet(queryset=Images.objects.none())
    context = {
        'form': form,
        'formset': formset,
    }
    return render(request, 'index.html', context)


def addProduto3(request):
    ImageForm2Set = modelformset_factory(Imagens, fields=('imagem',), extra=4)
    if request.method == 'POST':
        form = VeicleForm(request.POST)
        formset = ImageForm2Set(request.POST or None, request.FILES or None)
        if form.is_valid() and formset.is_valid():
            veicle = form.save(commit=False)
            veicle.save()

            for f in formset:
                try:
                    photo = Imagens(veicle=veicle, imagem=f.cleaned_data['imagem'])
                    photo.save()
                except Exception as e:
                    break
    else:
        form = VeicleForm()
        formset = ImageForm2Set(queryset=Imagens.objects.none())
    context = {
        'form': form,
        'formset': formset,
    }
    return render(request, 'index.html', context)
