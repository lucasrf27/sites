# Generated by Django 2.2.1 on 2019-06-24 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('c2vconfig', '0005_tutorial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='entendido',
            field=models.TextField(max_length=2000),
        ),
    ]
