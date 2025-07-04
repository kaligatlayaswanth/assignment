from rest_framework import serializers

class ChartDataSerializer(serializers.Serializer):
    labels = serializers.ListField(child=serializers.CharField())
    data = serializers.ListField(child=serializers.FloatField())
    description = serializers.CharField()  # Added to describe what the chart represents

class CardDataSerializer(serializers.Serializer):
    metric = serializers.CharField()
    value = serializers.FloatField()

class DemoDataSerializer(serializers.Serializer):
    financial = serializers.DictField()  # Financial data (bar, pie, cards)
    hr = serializers.DictField()        # HR data (bar, pie, cards)
    rd = serializers.DictField()        # R&D data (bar, pie, cards)
    security = serializers.DictField()  # Security data (bar, pie, cards)
    supply = serializers.DictField()    # Supply Chain data (bar, pie, cards)