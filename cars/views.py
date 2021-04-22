from django.shortcuts import render
from rest_framework import generics
from cars.serializers import *
from cars.models import *


class CarlistView(generics.ListAPIView):
    serializer_class = CarDetailSerializer
    queryset = Car.objects.all()


class CarCreateView(generics.CreateAPIView):
    serializer_class = CarDetailSerializer


class CarDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarDetailSerializer
    queryset = Car.objects.all()



