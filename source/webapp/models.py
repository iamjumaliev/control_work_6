from django.db import models

STATUS_CHOICES = [('active', 'Активно'), ('blocked', 'Заблокировоно')]

class Book(models.Model):

    name = models.CharField(max_length=300,null=False, blank=False, verbose_name='Имя')

    email = models.EmailField(max_length=300, null=False, blank=False, verbose_name='Почта')

    text = models.TextField(max_length=300, null=False, blank=False, verbose_name='Текст')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')

    status = models.CharField(max_length=20, verbose_name='статус', default=STATUS_CHOICES[0][0],
                              choices=STATUS_CHOICES)

    def __str__(self):
        return self.name

# Create your models here.
