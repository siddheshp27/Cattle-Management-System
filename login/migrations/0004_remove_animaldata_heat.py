# Generated by Django 4.0.2 on 2022-03-25 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_animaldata_heat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animaldata',
            name='heat',
        ),
    ]
