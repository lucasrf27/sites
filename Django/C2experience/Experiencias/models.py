from django.db import models
from django.urls import reverse


class Experiencias (models.Model):
    # nome da atividade#
    atividade = models.CharField(max_length=100)
    # numero da atividade# 2 primeiros para categoria os 3 para a atividade#
    serial = models.DecimalField(max_digits=5, decimal_places=3)
    # objetivo da atividade#
    topico = models.CharField(max_length=300)
    # dias disponiveis#
    avaible_days = models.DurationField(blank=True)
    # dia q começa#
    start_date = models.DateTimeField()
    # dia q termina#
    end_date = models.DateTimeField()
    # dia da ultima alteração#
    update_date = models.DateTimeField(auto_now=True)
    # foto da atividade#
    image = models.ImageField(upload_to='')
    # Preço#
    price = models.DecimalField(max_digits=7, decimal_places=2)

    def __repr__(self):
        return self.atividade, '-', self.serial

    def get_absolute_url(self):
        return reverse('home')
