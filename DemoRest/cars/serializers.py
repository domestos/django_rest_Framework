# конвертує дані з бази даних в формат JSON  і на оборот
from rest_framework import serializers
from cars.models import Car
class CarDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'
        
        