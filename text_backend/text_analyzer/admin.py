from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import ComparisonData, TextObjectData


class ComparisonDataAdmin(admin.ModelAdmin):
    list_display = ('label', 'text1', 'text2')


class TextObjectDataAdmin(admin.ModelAdmin):
    list_display = fields = ('label', 'author', 'top_n_words', 'top_p_puncs',
                             'top_s_sents', 'indexed_word_set', 'indexed_punc_set',
                             'average_word_length', 'average_sent_length', 'average_top_n_sent_length',
                             'sentence_lengths', 'sentence_length_freq')


admin.site.register(TextObjectData, TextObjectDataAdmin)
admin.site.register(ComparisonData, ComparisonDataAdmin)
