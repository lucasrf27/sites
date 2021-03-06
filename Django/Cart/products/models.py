from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.conf import settings


class Modelo(models.Model):
    P = 'P'
    M = 'M'
    G = 'G'
    tamanhos = [
        (P, 'P'),
        (M, 'M'),
        (G, 'G')
    ]


    CAMISA = 'CAMISA'
    REGATA = 'REGATA'
    VESTIDO = 'VESTIDO'
    MACACAO = 'MACACAO'
    CALSA = 'CALSA'
    SHORT = 'SHORT'
    INTIMA = 'INTIMA'
    tipo_choices = [
        (CAMISA, 'CAMISA'),
        (REGATA, 'REGATA'),
        (VESTIDO, 'VESTIDO'),
        (MACACAO, 'MACACAO'),
        (CALSA, 'CALSA'),
        (SHORT, 'SHORT'),
        (INTIMA, 'INTIMA'),
    ]


    Masculino = 'MASCULINO'
    Feminino = 'FEMININO'

    sexo_choice = [
        (Masculino, 'MASCULINO'),
        (Feminino, 'FEMININO')
    ]

    YEAR_CHOICES = []
    for r in range(0, 12):
        YEAR_CHOICES.append((r, r))

    Crianca = 'Crianca'
    Adulto = 'Adulto'

    publico_choice = [
        (Crianca, 'Crianca'),
        (Adulto, 'Adulto')
    ]


    modelo = models.CharField(max_length=7, choices=tipo_choices)
    publico = models.CharField(choices=publico_choice, max_length=7)
    sexo = models.CharField(choices=sexo_choice, max_length=9)
    idade_min = models.IntegerField(blank=True, choices=YEAR_CHOICES, default=0)
    tamanho = models.CharField(max_length=1, choices=tamanhos)

    def __str__(self):
            return '%s-%s-%s-%sanos' % (self.modelo, self.publico[0], self.tamanho, self.idade_min)


class Produto (models.Model):
    model = models.ForeignKey(Modelo, on_delete=models.CASCADE, related_name='mod')
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    created_time = models.DateTimeField(auto_now=True)
    updated_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.model, self.nome)

def get_image_filename(instance, filename):
    nome = instance.product.nome
    slug = slugify(nome)
    return "produto_imagens/%s-%s" % (slug, filename)


class Imagem (models.Model):
    product = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='prod')
    image = models.ImageField(upload_to=get_image_filename)


    