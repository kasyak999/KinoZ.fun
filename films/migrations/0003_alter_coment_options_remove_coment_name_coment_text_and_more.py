# Generated by Django 4.2.12 on 2024-08-10 21:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('films', '0002_coment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coment',
            options={'ordering': ('-created_at',), 'verbose_name': 'комментарии', 'verbose_name_plural': 'Комментарии'},
        ),
        migrations.RemoveField(
            model_name='coment',
            name='name',
        ),
        migrations.AddField(
            model_name='coment',
            name='text',
            field=models.TextField(blank=True, verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='coment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='coment',
            name='film',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coment', to='films.filmsdmodel', verbose_name='Фильм'),
        ),
    ]