from django.db import models


class Topping(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Название'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'


class FoodCategory(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Название'
    )
    is_publish = models.BooleanField(
        default=False
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория Блюд'
        verbose_name_plural = 'Категории Блюд'


class Food(models.Model):
    category = models.ForeignKey(
        FoodCategory, 
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='foods'
    )
    name = models.CharField(
        max_length=50,
        verbose_name='Название'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    price = models.IntegerField()
    is_special = models.BooleanField(
        default=False
    )
    is_vegan = models.BooleanField(
        default=False
    )
    is_publish = models.BooleanField(
        default=False
    )
    toppings = models.ManyToManyField(
        Topping,
        blank=True    
    )

    def __str__(self):
         return self.name

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'
