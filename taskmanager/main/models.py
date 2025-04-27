from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField( 'Название', max_length=200)
    task = models.TextField('Описание')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ['-created_at']

class Shedule(models.Model):
    фамилия = models.CharField(max_length=100)
    имя = models.CharField(max_length=100)
    отчество = models.CharField(max_length=100)
    телефон = models.CharField(max_length=20)
    почта = models.EmailField()
    кабинет = models.IntegerField()
    статус_кабинета = models.CharField(max_length=50)
    должность = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.фамилия} {self.имя}"