# Generated by Django 3.0 on 2020-03-23 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20200323_0412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelo',
            name='publico',
            field=models.CharField(choices=[('Crianca', 'Crianca'), ('Adulto', 'Adulto')], max_length=7),
        ),
    ]