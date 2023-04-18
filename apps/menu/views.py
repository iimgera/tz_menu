from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import (
    generics, 
    viewsets
)

from apps.menu.models import (
    FoodCategory,
    Topping, 
    Food
)
from apps.menu.serializers import (
    ToppingSerializer,
    FoodSerializer, 
    FoodCategorySerializer
)


class ToppingListAPIView(generics.ListAPIView):
    queryset = Topping.objects.all()
    serializer_class =ToppingSerializer


class FoodCategoryListAPIView(generics.ListAPIView):
    queryset = FoodCategory.objects.filter(is_publish=True).prefetch_related('foods')
    serializer_class = FoodCategorySerializer


class FoodListAPIView(generics.ListAPIView):
    queryset = Food.objects.filter(is_publish=True)
    serializer_class = FoodSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        is_vegan = self.request.query_params.get('is_vegan')
        if is_vegan is not None:
            queryset = queryset.filter(is_vegan=is_vegan)
        is_special = self.request.query_params.get('is_special')
        if is_special is not None:
            queryset = queryset.filter(is_special=is_special)
        toppings = self.request.query_params.getlist('topping')
        if toppings:
            queryset = queryset.filter(toppings__name__in=toppings)
        return queryset
