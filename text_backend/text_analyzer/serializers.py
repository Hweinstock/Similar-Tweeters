from rest_framework import serializers
from .models import ComparisonData, TextObjectData


class CompSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComparisonData
        fields = ('id', 'label', 'text1', 'text2', 'comp')


class TextObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextObjectData
        fields = ('id', 'label', 'author', 'top_n_words', 'top_p_puncs',
                  'top_s_sents', 'indexed_word_set', 'indexed_punc_set',
                  'average_word_length', 'average_sent_length', 'average_top_n_sent_length',
                  'sentence_lengths', 'sentence_length_freq')
