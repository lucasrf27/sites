# Generated by Django 2.2.1 on 2019-10-02 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('veicles', '0011_auto_20191002_0844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagens',
            name='veicle',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='veicles.Veiculos'),
        ),
    ]
