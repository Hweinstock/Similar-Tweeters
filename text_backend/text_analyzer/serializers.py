from rest_framework import serializers
from .models import ComparisonData, TextObjectData


class CompSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComparisonData
        fields = ('id', 'label', 'text1', 'text2', 'comp')


class TextObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextObjectData
        fields = ('label', 'author', 'text')
