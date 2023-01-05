from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class Buyer(AbstractUser):
    ...


class Task(models.Model):
    title = models.CharField("Название", max_length=50)
    task = models.TextField('Описание')
    data_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
