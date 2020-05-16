# Generated by Django 2.2.1 on 2019-09-19 03:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('veicles', '0003_auto_20190919_0001'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('CARRO', 'CARRO'), ('MOTO', 'MOTO'), ('OUTRO', 'OUTRO')], default='CARRO', max_length=5)),
                ('veicle', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='veicles.Veiculos', verbose_name='imagens do veiculo')),
            ],
        ),
    ]