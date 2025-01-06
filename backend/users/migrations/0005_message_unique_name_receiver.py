# Generated by Django 5.1.4 on 2025-01-06 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_message_options_alter_message_content_and_more'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='message',
            constraint=models.UniqueConstraint(fields=('sender', 'receiver'), name='unique_name_receiver'),
        ),
    ]
