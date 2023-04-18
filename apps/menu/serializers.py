from rest_framework import serializers

from apps.menu.models import (
    Topping,
    Food,
    FoodCategory
)


class ToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topping
        fields = (
            'id',
            'name'
        )


class FoodSerializer(serializers.ModelSerializer):
    toppings = ToppingSerializer(many=True)
    category = ToppingSerializer(many=True)

    class Meta:
        model = Food
        fields = (
            'id',
            'category',
            'name',
            'description',
            'price',
            'is_special',
            'is_vegan',
            'is_publish',
            'toppings'
        )
            

class FoodCategorySerializer(serializers.ModelSerializer):
    foods = FoodSerializer(many=True)
    class Meta:
        model = FoodCategory
        fields = (
            'id',
            'name',
            'is_publish',
            'foods'
         )
 
