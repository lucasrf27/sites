from django import forms
from .models import Componentes, Imagens, Veiculos
from datetime import datetime


class VeicleForm(forms.ModelForm):
    YEAR_CHOICES = []
    for r in range(1960, (datetime.now().year+1)):
        YEAR_CHOICES.append((r, r))

    modelo = forms.CharField(max_length=100)
    potencia = forms.CharField(max_length=40)
    cor = forms.CharField(max_length=30)
    preco = forms.DecimalField(max_digits=8, decimal_places=2)
    ano = forms.IntegerField()
    category = forms.ChoiceField()
    first_gallery = forms.BooleanField()
    mini_gallery = forms.BooleanField()

    class Meta:
        prefix = 'veicle'
        model = Veiculos
        fields = ('modelo', 'potencia', 'cor', 'preco', 'ano', 'first_gallery', 'mini_gallery')


class ImageForm(forms.ModelForm):
    imagem = forms.ImageField(label='Image')

    class Meta:
        model = Imagens
        fields = ('imagem', )
