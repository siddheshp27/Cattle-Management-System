# Generated by Django 4.0.2 on 2022-03-23 18:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_remove_animaldata_heat'),
    ]

    operations = [
        migrations.AddField(
            model_name='animaldata',
            name='heat',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]