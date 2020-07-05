from django.db import models
from products.models import Produto
from django.contrib.auth import get_user_model
from .managers import ItemManager

User = get_user_model()

class Pedido(models.Model):
    ref_code = models.CharField(max_length=15)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default=False)
    date_ordered = models.DateTimeField(auto_now=True)

    def get_cart_total(self):
        total = 0
        for item in self.order_items.all():
            total_item = item.product.preco * item.quantity
            total += total_item
        return total

    def __str__(self):
        return '{0} - {1}'.format(self.owner, self.ref_code)


class Item(models.Model):
    product = models.ForeignKey(Produto, on_delete=models.SET_NULL, null=True, related_name='product_items')
    order = models.ForeignKey(Pedido, on_delete=models.SET_NULL, null=True, related_name='order_items')
    is_ordered = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)
    date_ordered = models.DateTimeField(null=True)
    quantity = models.PositiveIntegerField(default=1)
    objects = ItemManager()

    def __str__(self):
        return '{} -> {} '.format(self.product, self.order)

    def get_item_total(self):
        return self.product.preco * self.quantity
