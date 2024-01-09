from django.db import models

from config import settings

NULLABLE = {'blank': True, 'null': True}


class Module(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE, verbose_name='создатель')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'образовательный модуль'
        verbose_name_plural = 'образовательные модули'
