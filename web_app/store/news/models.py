from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class Animals(models.Model):
    name = models.CharField('Имя', max_length=100)
    age = models.IntegerField('Возраст')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    color = models.ManyToManyField('Color')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/news/'

    class Meta:
        verbose_name = 'Животное'
        verbose_name_plural = 'Животные'


class Category(models.Model):
    name = models.CharField('Вид животного', max_length=100)
    id_breed = models.OneToOneField('Breed', on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'



class Color(models.Model):
    name = models.CharField('Цвет животного', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'

class Breed(models.Model):
    name = models.CharField('Порода животного', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Порода'
        verbose_name_plural = 'Породы'


class User(AbstractUser):
    role = models.CharField('Роль пользователя', max_length=200, default='user')
