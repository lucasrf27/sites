from rest_framework import serializers

class CarSerializer(serializers.Serializer):
    brand = serializers.EmailField()
    year = serializers.IntegerField()
    created_time = serializers.DateTimeField()
