from django.db import models
from phone_field import PhoneField
from datetime import datetime
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse



get_user_model = User

class Parceiros (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    endereco = models.TextField(max_length=400, blank=True)
    responsavel = models.CharField(max_length=100)
    tel = PhoneField(max_length=12)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)
    ativo = models.BooleanField(default=False)

    def get_queryset(self):
        queryset = super(Parceiros, self).get_queryset()
        return queryset

    def __str__(self):
        return '%s %s' % (self.user, self.nome)

    def get_absolute_url(self):
        return reverse('parceiro_detail2', kwargs={'pk': self.pk})


class Servicos (models.Model):
    parceiro = models.ForeignKey(Parceiros, on_delete=models.CASCADE, related_name='servi')
    tipo = models.CharField(max_length=200)
    objetivo = models.TextField(max_length=500, blank=True)
    preco = models.DecimalField(max_digits=9, decimal_places=2, blank=True)
    telefone = PhoneField(max_length=12, default='21968151502')

    def __str__(self):
        return '%s %s' % (self.tipo, self.parceiro)
        
def get_image_filename(instance, filename):
    tipo = instance.servicos.tipo
    slug = slugify(tipo)
    return "servicos_imagens/%s-%s" % (slug, filename)


class Imagens (models.Model):
    servicos = models.ForeignKey(Servicos, on_delete=models.CASCADE, related_name='images')
    imagem = models.ImageField(upload_to=get_image_filename)
