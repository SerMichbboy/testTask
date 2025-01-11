from django.db import models

class Task(models.Model):
    """
        Модель для хранения задач:
        - title: Название задачи (строка, максимум 100 символов).
        - is_completed: Статус выполнения задачи (логическое, по умолчанию False).
    """
    title = models.CharField(
        max_length=100, 
        verbose_name='Название задачи'
    )
    is_completed = models.BooleanField(
        default=False,
        verbose_name='Статус выполнения'
    )
