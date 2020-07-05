# Generated by Django 3.0 on 2020-06-16 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_produto_quantidade'),
        ('cart', '0003_item_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='product',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='item', to='products.Produto'),
        ),
    ]