# Generated by Django 5.1.4 on 2025-01-07 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Добавлен')),
                ('name', models.CharField(max_length=256, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'Категории',
                'ordering': ('name',),
                'abstract': False,
                'default_related_name': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Coment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Добавлен')),
            ],
            options={
                'verbose_name': 'комментарии',
                'verbose_name_plural': 'Комментарии',
                'ordering': ('-created_at',),
                'abstract': False,
                'default_related_name': 'coments',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Добавлен')),
                ('name', models.CharField(max_length=256, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'страна',
                'verbose_name_plural': 'Страны',
                'ordering': ('name',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Добавлен')),
            ],
            options={
                'verbose_name': 'избраное',
                'verbose_name_plural': 'Избраное',
                'default_related_name': 'favorites',
            },
        ),
        migrations.CreateModel(
            name='FilmsdModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Добавлен')),
                ('name', models.CharField(max_length=256, verbose_name='Название')),
                ('verified', models.BooleanField(default=False, help_text='Снимите галочку, если все проверено.', verbose_name='Проверено')),
                ('is_published', models.BooleanField(default=False, help_text='Снимите галочку, чтобы скрыть публикацию.', verbose_name='Опубликовано')),
                ('id_kp', models.IntegerField(unique=True, verbose_name='id кинопоиска')),
                ('name_orig', models.CharField(blank=True, max_length=256, null=True, verbose_name='Оригинальное название')),
                ('year', models.IntegerField(blank=True, null=True, verbose_name='Год')),
                ('poster', models.TextField(blank=True, help_text='Пример: http://оригинал, http://превью', null=True, verbose_name='Постер')),
                ('rating', models.FloatField(blank=True, default=0, null=True, verbose_name='Рейтинг')),
                ('votecount', models.IntegerField(blank=True, default=0, null=True, verbose_name='Голосов')),
                ('description', models.TextField(blank=True, default='Нет описания', null=True, verbose_name='Описание')),
                ('scrinshot', models.JSONField(blank=True, help_text='imageUrl - оригинал, "previewUrl - превью[{"imageUrl": "ссылка", "previewUrl": "ссылка"}, ]', null=True, verbose_name='Скриншоты')),
                ('actors', models.TextField(blank=True, null=True, verbose_name='Актеры')),
            ],
            options={
                'verbose_name': 'фильм',
                'verbose_name_plural': 'Фильмы',
                'ordering': ('-created_at',),
                'abstract': False,
                'default_related_name': 'posts',
            },
        ),
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Добавлен')),
                ('name', models.CharField(max_length=256, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'жанр',
                'verbose_name_plural': 'Жанры',
                'ordering': ('name',),
                'abstract': False,
            },
        ),
    ]
