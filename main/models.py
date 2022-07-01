from tabnanny import verbose
from django.db import models


class Task(models.Model):
    title = models.CharField('Name', max_length=200)
    task = models.TextField('Description')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'To do list'