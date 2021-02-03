from django.db import models
import json
# Create your models here.


class TextObjectData(models.Model):
    label = models.CharField(max_length=120)
    author = models.CharField(max_length=120)

    top_n_words = models.JSONField()
    top_p_puncs = models.JSONField()
    top_s_sents = models.JSONField()

    indexed_word_set = models.JSONField()
    indexed_punc_set = models.JSONField()

    average_word_length = models.FloatField()
    average_sent_length = models.FloatField()
    average_top_n_sent_length = models.FloatField()

    sentence_lengths = models.JSONField()
    sentence_length_freq = models.JSONField()


class ComparisonData(models.Model):
    label = models.CharField(max_length=120)
    text1 = models.TextField()
    text2 = models.TextField()


