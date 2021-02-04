from django.db import models

from text_model.config_files.config import get_text_object
from text_model.analyzer.text_objects.text import analyze_config
# Create your models here.


class TextObjectData(models.Model):
    label = models.CharField(max_length=120)
    author = models.CharField(max_length=120)
    text = models.TextField(default='')

    def to_text_object(self):
        obj = get_text_object(self.label)

        return obj(author=self.author, filepath_or_text=self.text, raw_text=True)


class ComparisonData(models.Model):
    label = models.CharField(max_length=120)
    text1 = models.IntegerField(models.ForeignKey('TextObjectData',
                                                  on_delete=models.CASCADE))
    text2 = models.IntegerField(models.ForeignKey('TextObjectData',
                                                  on_delete=models.CASCADE))


