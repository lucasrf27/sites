# Generated by Django 2.2.1 on 2019-07-08 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('c2vconfig', '0006_auto_20190624_0441'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tutorial',
            old_name='entendido',
            new_name='code',
        ),
    ]