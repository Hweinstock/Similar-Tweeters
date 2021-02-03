from django.db import models
import json
# Create your models here.


class TextObjectData(models.Model):
    label = models.CharField(max_length=120)
    author = models.CharField(max_length=120)
    text = models.TextField(default='')


class ComparisonData(models.Model):
    label = models.CharField(max_length=120)
    text1 = models.TextField()
    text2 = models.TextField()


