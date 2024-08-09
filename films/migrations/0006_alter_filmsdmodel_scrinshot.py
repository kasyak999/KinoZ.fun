# Generated by Django 4.2.12 on 2024-08-08 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0005_alter_filmsdmodel_scrinshot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filmsdmodel',
            name='scrinshot',
            field=models.TextField(blank=True, help_text='imageUrl - оригинал, "previewUrl - превью[{"imageUrl": "ссылка", "previewUrl": "ссылка"}, ]', null=True, verbose_name='Скриншоты'),
        ),
    ]
