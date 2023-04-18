from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.menu.models import (
    Topping,
    FoodCategory,
    Food
)


class ToppingAdmin(admin.ModelAdmin):
    list_display = (
        'id', 
        'name'
    )


class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name', 
        'is_publish'
    )


class FoodAdmin(admin.ModelAdmin):
    list_display = (
        'name', 
        'category', 
        'description', 
        'price', 
        'is_special', 
        'is_vegan', 
        'is_publish', 
        'get_toppings'
    )
    
    filter_horizontal = ('toppings', )

    def get_toppings(self, obj):
        return ", ".join([str(t) for t in obj.toppings.all()])
    get_toppings.short_description = 'Toppings'


admin.site.register(Topping, ToppingAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(FoodCategory, FoodCategoryAdmin)
