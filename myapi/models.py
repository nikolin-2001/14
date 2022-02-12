from django.db import models

class Yasherka(models.Model):
    name = models.CharField('название', max_length=240)
    image = models.TextField('URL изоображения', max_length=5000)
    date = models.CharField('Дата', max_length=200)

class Pashalkaone(models.Model):
    text = models.TextField('Текст', max_length=5000)


class Pashalkatwo(models.Model):
    text = models.TextField('Текст', max_length=5000)