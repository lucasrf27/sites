# Generated by Django 3.0 on 2020-03-23 04:53

from django.db import migrations, models
import django.db.models.deletion
import products.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(choices=[('CAMISA', 'CAMISA'), ('REGATA', 'REGATA'), ('VESTIDO', 'VESTIDO'), ('MACACAO', 'MACACAO'), ('CALSA', 'CALSA'), ('SHORT', 'SHORT'), ('INTIMA', 'INTIMA')], max_length=7)),
                ('criança', models.BooleanField(blank=True)),
                ('adulto', models.BooleanField(blank=True)),
                ('sexo', models.BooleanField(choices=[('MASCULINO', 'MASCULINO'), ('FEMININO', 'FEMININO')])),
                ('idade_min', models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11)], max_length=2)),
                ('tamanho', models.CharField(choices=[('P', 'P'), ('M', 'M'), ('G', 'G')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=5)),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mod', to='products.Modelo')),
            ],
        ),
        migrations.CreateModel(
            name='Imagens',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=products.models.get_image_filename)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prod', to='products.Produto')),
            ],
        ),
    ]