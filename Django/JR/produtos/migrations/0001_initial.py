# Generated by Django 2.1.7 on 2019-04-09 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('preço', models.DecimalField(decimal_places=2, max_digits=5)),
                ('foto', models.ImageField(upload_to='')),
            ],
        ),
    ]
