from django.db import models


class SleepPoint(models.Model):
    class EventType(models.TextChoices):
        UP = "UP", "Подьем"
        DOWN = "DOWN", "Отбой"

    event = models.CharField(
        max_length=4, verbose_name="Событие", choices=EventType.choices
    )
    date = models.DateField(verbose_name="Дата")
    time = models.TimeField(verbose_name="Время")

    class Meta:
        verbose_name = "Точка сна"
        verbose_name_plural = "Точки сна"
