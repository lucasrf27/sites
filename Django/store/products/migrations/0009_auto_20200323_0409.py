# Generated by Django 3.0 on 2020-03-23 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20200323_0409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelo',
            name='publico',
            field=models.IntegerField(choices=[('C', 'Crianca'), ('A', 'Adulto')], default=2),
        ),
    ]