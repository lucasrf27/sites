from django import forms
from .models import Post, Images
from .models import Imagens, Veiculos
from datetime import datetime


class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=128)
    body = forms.CharField(max_length=245, label="Item Description.")

    class Meta:
        model = Post
        fields = ('title', 'body', )


class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')

    class Meta:
        model = Images
        fields = ('image', )


class VeicleForm(forms.ModelForm):
    YEAR_CHOICES = []
    for r in range(1960, (datetime.now().year+1)):
        YEAR_CHOICES.append((r, r))

    modelo = forms.CharField(max_length=100)
    potencia = forms.CharField(max_length=40)
    cor = forms.CharField(max_length=30)
    preco = forms.DecimalField(max_digits=8, decimal_places=2)
    ano = forms.IntegerField()

    class Meta:
        prefix = 'veicle'
        model = Veiculos
        fields = ('modelo', 'potencia', 'cor', 'preco', 'ano')


class ImageForm2(forms.ModelForm):
    imagem = forms.ImageField(label='Image')

    class Meta:
        model = Imagens
        fields = ('imagem', )
