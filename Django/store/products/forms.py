from django import forms
from .models import Modelo, Produto, Imagem, Banner, BannerImages



class ModeloForm(forms.ModelForm):
    class Meta:
        model = Modelo
        fields = ['modelo', 'publico', 'sexo', 'idade_min', 'tamanho']


class ProdutoForm(forms.ModelForm):
    nome = forms.CharField(max_length=100)
    preco = forms.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        model = Produto
        fields = ['model', 'nome', 'preco', 'mini_gallery']



class ImagemForm(forms.ModelForm):
    image = forms.ImageField(label='Image')

    class Meta:
        model = Imagem
        fields = ('image', )



class BannerForm(forms.ModelForm):
    Inicial = 'Inicial'
    Mini = 'Mini'
    Adjacentes = 'Adjacentes'
    Promocao = 'Promocao'
    tipos_banner = [
        (Inicial, 'Inicial'),
        (Mini, 'Mini'),
        (Promocao, 'Promocao'),
        (Adjacentes, 'Adjacentes'),
    ]
    nome = forms.CharField(max_length=100)
    tipo = forms.ChoiceField(choices=tipos_banner)

    class Meta:
        model = Banner
        fields = ('nome', 'tipo')


class BannerImagesForm(forms.ModelForm):
    imagem = forms.ImageField(label='banner_image')

    class Meta:
        model = BannerImages
        fields = ('bannering', 'imagem')