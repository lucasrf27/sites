from django.db import models


class ProdutoManager(models.Manager):
    def price_low(self, preco):
        return self.filter(preco__lt=preco)

    def get_by_modelo(self, tipo):
        big = tipo.upper()
        return self.filter(model__modelo=big)