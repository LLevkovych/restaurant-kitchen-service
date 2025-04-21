from django.contrib import admin

from core.models import DishType, Dish, Ingredient

admin.site.register(DishType)
admin.site.register(Dish)
admin.site.register(Ingredient)

