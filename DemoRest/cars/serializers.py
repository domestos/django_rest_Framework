# конвертує дані з бази даних в формат JSON  і на оборот
from rest_framework import serializers
from cars.models import Car
class CarDetailSerializer(serializers.ModelSerializer):
    # приховати поле і задати значення по дефолку (serializers.CurrentUserDefault - отримує ям"я залогованого юзера)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Car
        fields = '__all__'
        

class CarListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('id', 'vin', 'user')