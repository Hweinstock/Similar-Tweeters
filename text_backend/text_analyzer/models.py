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

    def _get_comp(self):

        # TextObject = get_text_object(self.label)
        # Text1 = TextObject(self.text1, raw_text=True)
        # Text2 = TextObject(self.text2, raw_text=True)
        # CompObject = Comparison(Text1, Text2)
        return "Hello World"

        # Create TextObjects
        # Create Comparison Object
        # Load Model
        # Make Prediction
        # Return Prediction
        pass

    comp = property(_get_comp)

    def _str_(self):
        return str({'label': self.label,
                    'text1': self.text1,
                    'text2': self.text2,
                    'comp': self.comp})

