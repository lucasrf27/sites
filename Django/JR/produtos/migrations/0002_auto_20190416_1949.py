# Generated by Django 2.1.7 on 2019-04-16 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='foto',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]