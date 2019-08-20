from django.shortcuts import render
from rest_framework import generics
from cars.serializers import CarDetailSerializer, CarListSerializer
from cars.models import Car
# кастомний клас перевіряє власника посту і повертає boolian 
from cars.permissions import IsOwnerOrReadOnly
#
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from rest_framework.authentication import TokenAuthentication, SessionAuthentication
#===================== Auth
   # Щоб не дублювати у всіх класах метод аутентифікації, його можна пропиати один раз у settings
   # authentication_classes = (TokenAuthentication, SessionAuthentication )

# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': [
#         'rest_framework.authentication.BasicAuthentication',
#         'rest_framework.authentication.SessionAuthentication',
#         'rest_framework.authentication.TokenAuthentication',
#     ]
# }
   

# Create your views here.
# CREATE -- POST
class CarCreateView(generics.CreateAPIView):
    serializer_class = CarDetailSerializer

# GET ALL -- GET
class CarListView(generics.ListAPIView):
    serializer_class = CarListSerializer
    # generics.ListAPIView -- має обов"язковий параметр queryset
    queryset = Car.objects.all()
    # Лише авторизовані юзери можуть переглядати список машині
    permission_classes = (IsAuthenticated,  )

# UPDATE/DELETE  -- PUT/DELETE
class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarDetailSerializer
    queryset = Car.objects.all()
    # Даний клас API доспуний лише через аунтифікацію по Токену (можна розширити аунтифікацію - добавити SessionAuthentication)
    authentication_classes = (TokenAuthentication, )
    # редагувати обєкт може лише власник і суперюзер
    permission_classes = (IsOwnerOrReadOnly, IsAdminUser )
    