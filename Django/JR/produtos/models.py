from django.db import models


class Produto (models.Model):
    nome = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    foto = models.ImageField(blank=True, upload_to='')
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    YEAR_IN_SCHOOL_CHOICES = [
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
    ]
    year_in_school = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=FRESHMAN,
    )

    def is_upperclass(self):
        return self.year_in_school in (self.JUNIOR, self.SENIOR)

    def __repr__(self):
        return self.nome + '-' + self.year_in_school


class Classifica (models.Model):
    nome = models.CharField(max_length=100)
    preço = models.DecimalField(decimal_places=2, max_digits=3)
    imagens = models.ImageField(upload_to='', blank=True)
    # choice field#
    MUITO_IMPORTANTE = '5'
    IMPORTANTE = '4'
    SUAVE = '3'
    RELAXA = '2'
    PRA_DEPOIS = '1'
    field_choices = [
        (MUITO_IMPORTANTE, 'MUITO_IMPORTANTE'),
        (IMPORTANTE, 'IMPORTANTE'),
        (SUAVE, 'SUAVE'),
        (RELAXA, 'RELAXA'),
        (PRA_DEPOIS, 'PRA DEPOIS'),
    ]
    urgencia = models.CharField(choices=field_choices, blank=False, max_length=40)
