from django.db import models


class Product_sell_create(models.Model):
    product_product_sell = models.CharField(max_length=120)
    product_price_sell = models.DecimalField(decimal_places=2, max_digits=500)
    product_volume_sell = models.DecimalField(decimal_places=2, max_digits=500)
    product_location_sell = models.CharField(max_length=120)
    product_description_sell = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.product_product_sell