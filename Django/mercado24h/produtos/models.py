from django.db import models


class Categoria (models.Model):
    categoria = models.CharField(max_length=30)
    icone = models.ImageField(upload_to='')


class Produto (models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    imagem = models.ImageField(upload_to='')
    descricao = models.CharField(max_length=200)
    estoque = models.IntegerField(blank=True)
    em_falta = models.BooleanField(blank=True)
    categorias = models.ManyToManyField(Categoria)

    def __str__(self):
        return self.nome + '-' + self.preco
