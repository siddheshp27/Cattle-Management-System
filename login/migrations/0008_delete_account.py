# Generated by Django 4.0.2 on 2022-03-26 21:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_account'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Account',
        ),
    ]