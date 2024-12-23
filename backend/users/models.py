from django.contrib.auth.models import AbstractUser
from django.db import models


class UserProfile(AbstractUser):
    avatar = models.ImageField(
        upload_to='users/', null=True, blank=True,
        verbose_name='Аватар')

    class Meta:
        """Перевод модели"""

        verbose_name = 'пользователя'
        verbose_name_plural = 'Пользователи'
        ordering = ('username',)

    def __str__(self):
        return self.username
