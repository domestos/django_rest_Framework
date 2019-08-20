
from django.contrib import admin
from django.urls import path
from django.urls import include
from .views import CarCreateView, CarListView, CarDetailView
app_name = 'car'
urlpatterns = [
    path('car/create/', CarCreateView.as_view() ),
    path ('all/', CarListView.as_view() ),
    # <int:pk>  - integet:primary key 
    path ('car/detail/<int:pk>/', CarDetailView.as_view())
]
