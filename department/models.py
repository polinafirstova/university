from django.db import models
from django.contrib.auth import get_user_model


class Teacher(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name='Имя преподавателя'
    )
    image = models.ImageField(
        upload_to='teachers/',
        blank=True,
        null=True,
        verbose_name='Изображение'
    )
    position = models.CharField(
        max_length=256,
        verbose_name='Должность'
    )
    full_time = models.BooleanField(
        default=True,
        verbose_name='Работа на полную ставку',
        help_text=''.join([
            'Уберите галочку, ',
            'если преподаватель работает не на полную ставку'
        ])
    )
    additional_work = models.TextField(
        blank=True,
        null=True,
        verbose_name='Дополнительная работа'
    )
    audience = models.ForeignKey(
        'Audience',
        on_delete=models.CASCADE,
        verbose_name='Аудитория'
    )
    courses = models.ManyToManyField(
        'Course',
        related_name='teachers',
        verbose_name='Курсы'
    )

    class Meta:
        verbose_name = 'преподаватель'
        verbose_name_plural = 'преподаватели'
        ordering = ['name']

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name='Название курса'
    )
    description = models.TextField(
        blank=True,
        verbose_name='Описание курса'
    )

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'
        ordering = ['name']

    def __str__(self):
        return self.name


class Audience(models.Model):
    number = models.CharField(
        max_length=5,
        verbose_name='Номер преподавательской'
    )  

    class Meta:
        verbose_name = 'преподавательская'
        verbose_name_plural = 'преподавательские'
        ordering = ['number']

    def __str__(self):
        return self.number