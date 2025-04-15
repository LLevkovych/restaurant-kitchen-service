from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from core.models import DishType, Cook, Dish

@login_required
def index(request):
    num_cooks = Cook.objects.count()
    num_dishes = Dish.objects.count()
    num_dish_types = DishType.objects.count()

    context = {
        "num_drivers": num_cooks,
        "num_cars": num_dishes,
        "num_manufacturers": num_dish_types,
    }

    return render(request, "core/index.html", context=context)
