# Generated by Django 2.2.1 on 2019-09-04 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('c2vconfig', '0001_initial'), ('c2vconfig', '0002_auto_20190603_2147')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MP4',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('preço', models.DecimalField(decimal_places=2, max_digits=5)),
                ('imagem', models.ImageField(blank=True, upload_to='media')),
                ('artista', models.CharField(max_length=100, null=True)),
                ('url', models.URLField(default='unknow', max_length=300)),
            ],
        ),
    ]