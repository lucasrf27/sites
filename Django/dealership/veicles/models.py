from django.db import models
from datetime import datetime
from django.urls import reverse
from django.template.defaultfilters import slugify


class Veiculos (models.Model):
    CARRO = 'CARRO'
    MOTO = 'MOTO'
    OUTRO = 'OUTRO'
    field_choices = [
        (CARRO, 'CARRO'),
        (MOTO, 'MOTO'),
        (OUTRO, 'OUTRO'),
    ]

    YEAR_CHOICES = []
    for r in range(1960, (datetime.now().year+1)):
        YEAR_CHOICES.append((r, r))

    modelo = models.CharField(max_length=100)
    potencia = models.CharField(max_length=40)
    cor = models.CharField(max_length=30)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    ano = models.IntegerField(('ano'), choices=YEAR_CHOICES, default=datetime.now().year)
    created_time = models.DateTimeField(auto_now=True)
    updated_time = models.DateTimeField(auto_now_add=True)
    category = models.CharField(
        max_length=5,
        default=CARRO,
        choices=field_choices)
    first_gallery = models.BooleanField(null=True)
    mini_gallery = models.BooleanField(null=True)

    def __str__(self):
        return '%s %s' % (self.modelo, self.preco)

    def get_absolute_url(self):
        return reverse('category2')

    def first_image(self):
        return self.images.first()  

    def second_image(self):
        return self.images.all()[1]
    
    def third_image(self):
        return self.images.all()[2]

    def fourth_image(self):
        return self.images.all()[3]

def get_image_filename(instance, filename):
    modelo = instance.veicle.modelo
    slug = slugify(modelo)
    return "veiculos_imagens/%s-%s" % (slug, filename)


class Imagens (models.Model):
    veicle = models.ForeignKey(Veiculos, default=None, on_delete=models.CASCADE, related_name='images')
    imagem = models.ImageField(upload_to=get_image_filename)
    

class Componentes (models.Model):
    veicle = models.ForeignKey(Veiculos, related_name='componentes', on_delete=models.CASCADE)
    componente = models.CharField(max_length=200)


    def __str__(self):
        return '%s - %s' % (self.componente, self.veicle)
