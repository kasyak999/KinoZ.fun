# Generated by Django 5.0.7 on 2024-08-06 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='filmsdmodel',
            old_name='id_kp',
            new_name='kinopoisk',
        ),
    ]
