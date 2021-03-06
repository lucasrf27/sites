# Generated by Django 2.2.6 on 2019-11-21 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('veicles', '0016_remove_categorias_veicle'),
    ]

    operations = [
        migrations.CreateModel(
            name='Componentes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('componente', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='veiculos',
            name='category',
        ),
        migrations.AddField(
            model_name='veiculos',
            name='category',
            field=models.CharField(choices=[('CARRO', 'CARRO'), ('MOTO', 'MOTO'), ('OUTRO', 'OUTRO')], default='CARRO', max_length=5),
        ),
        migrations.DeleteModel(
            name='Categorias',
        ),
        migrations.AddField(
            model_name='componentes',
            name='veicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='componentes', to='veicles.Veiculos'),
        ),
    ]
