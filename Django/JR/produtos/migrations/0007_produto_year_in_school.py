# Generated by Django 2.2.1 on 2019-06-24 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0006_auto_20190622_1943'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='year_in_school',
            field=models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior')], default='FR', max_length=2),
        ),
    ]
