# Generated by Django 2.1.7 on 2019-05-15 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0003_auto_20190416_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='foto',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
    ]