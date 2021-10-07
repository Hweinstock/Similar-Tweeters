from django.db import models

from .text_model.config_files.config import get_text_object
from .text_model.analyzer.comparison import Comparison as CompObject
from .text_model.analyzer.model.model import run_on_object
# Create your models here.


class TextObjectData(models.Model):
    label = models.CharField(max_length=120)
    author = models.CharField(max_length=120)
    source = models.CharField(max_length=120)
    text = models.TextField(default='')

    def to_text_object(self):
        obj = get_text_object(self.label)

        return obj(author=self.author, filepath_or_text=self.text, raw_text=True)


class ComparisonData(models.Model):
    label = models.CharField(max_length=120)
    source = models.CharField(max_length=120, default="unknown")
    text1 = models.ForeignKey(TextObjectData, on_delete=models.CASCADE, related_name='text_1')
    text2 = models.ForeignKey(TextObjectData, on_delete=models.CASCADE, related_name='text_2')

    def to_comp_object(self):
        text1_vec = self.text1.to_text_object().to_vector
        text2_vec = self.text2.to_text_object().to_vector

        comp_object = CompObject(text1_vec, text2_vec)

        return comp_object

    def run_on_model(self):
        comp_object = self.to_comp_object()
        result, percent = run_on_object(comp_object)

        return result, percent



