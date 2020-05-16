from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.urls import reverse
from django.template.defaultfilters import slugify


class Post(models.Model):
    title = models.CharField(max_length=128)
    body = models.CharField(max_length=400)

    def __str__(self):
        return self.title


def get_image_filename(instance, filename):
    title = instance.post.title
    slug = slugify(title)
    return "post_images/%s-%s" % (slug, filename)


class Images(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_image_filename,
                              verbose_name='Image')


class Veiculos (models.Model):
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

    def __str__(self):
        return '%s %s' % (self.modelo, self.preco)

    def get_absolute_url(self):
        return reverse('category2')


def get_image_filename(instance, filename):
    modelo = instance.veicle.modelo
    slug = slugify(modelo)
    return "veiculos_imagens/%s-%s" % (slug, filename)


class Imagens (models.Model):
    veicle = models.ForeignKey(Veiculos, default=None, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to=get_image_filename, verbose_name='image')
