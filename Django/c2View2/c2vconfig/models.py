from django.db import models
from datetime import datetime
from django.urls import reverse


class MP4 (models.Model):
    nome = models.CharField(max_length=100)
    url = models.URLField(max_length=300)
    preço = models.DecimalField(max_digits=5, decimal_places=2)
    imagem = models.ImageField(upload_to='', blank=True)
    artista = models.CharField(max_length=100, default='Unknown')

    def __str__(self):
        return self.nome + '-' + self.artista

    def get_absolute_url(self):
        return reverse('MP4')


class Tutorial (models.Model):
    assunto = models.CharField(max_length=100)
    url = models.URLField(max_length=350)
    preview = models.TextField(max_length=200)
    data = models.DateField(default=datetime.today)
    code = models.TextField(max_length=2000)
    #  choice Field #
    ENGLISH = 'ENG'
    PORTUGUES = 'PT'
    OUTRO = 'QQ'
    field_choices = [
        (ENGLISH, 'INGLES'),
        (PORTUGUES, 'PORTUGUES'),
        (OUTRO, 'QUALQUER'),
    ]
    idioma = models.CharField(
        max_length=3,
        default=OUTRO,
        choices=field_choices)
        
    def __str__(self):
        return self.assunto + '-' + self.preview

    def is_upperclass(self):
        return self.idioma in (self.ENGLISH, self.PORTUGUES, self.OUTRO)

    def get_absoute_url(self):
        return reverse('tutorial', kwargs={'pk': self.pk})
