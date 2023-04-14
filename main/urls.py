from django.contrib import admin
from django.urls import path, include
from rest_framework import (
    routers, 
    permissions
)
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from apps.menu.views import (
    FoodListAPIView, 
    FoodCategoryListAPIView, 
    ToppingListAPIView
)


schema_view = get_schema_view(
    openapi.Info(
        title="API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc'),

    path('toppings/', ToppingListAPIView.as_view(), name='toppings'),
    path('food_categories/', FoodCategoryListAPIView.as_view(), name='food-categories'),
    path('foods/', FoodListAPIView.as_view(), name='foods'),
]

