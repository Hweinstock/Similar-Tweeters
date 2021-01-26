from rest_framework import serializers
from .models import ComparisonData


class CompSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComparisonData
        fields = ('id', 'label', 'text1', 'text2', 'comp')