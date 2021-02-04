from rest_framework import serializers
from .models import ComparisonData, TextObjectData


class CompSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComparisonData
        fields = ('id', 'label', 'text1_id', 'text2_id')


class TextObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextObjectData
        fields = ('id', 'label', 'author', 'text')
