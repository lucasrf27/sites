# Generated by Django 3.0 on 2020-02-02 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_auto_20200201_0659'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicos',
            old_name='parceiros',
            new_name='parceiro',
        ),
        migrations.AddField(
            model_name='parceiros',
            name='ativo',
            field=models.BooleanField(default=False),
        ),
    ]
