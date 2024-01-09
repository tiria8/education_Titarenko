from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None

    user_email = models.EmailField(unique=True, verbose_name='почта')
    user_phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    user_avatar = models.ImageField(upload_to='media/', verbose_name='аватар', **NULLABLE)
    user_city = models.CharField(max_length=100, verbose_name='город', **NULLABLE)
    is_active = models.BooleanField(default=True, verbose_name='Статус пользователя')

    USERNAME_FIELD = "user_email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.user_email

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
