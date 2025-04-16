from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views import generic

from core.models import DishType, Cook, Dish

@login_required
def index(request):
    num_cooks = Cook.objects.count()
    num_dishes = Dish.objects.count()
    num_dish_types = DishType.objects.count()

    context = {
        "num_cook": num_cooks,
        "num_dishes": num_dishes,
        "num_dish_types": num_dish_types,
    }

    return render(request, "core/index.html", context=context)


class DishTypeListView(generic.ListView):
    model = DishType
    template_name = "core/dish_type_list_view.html"
    context_object_name = "dish_type_list"


class CookListView(generic.ListView):
    model = Cook


class DishListView(generic.ListView):
    model = Dish
    queryset = Dish.objects.select_related("dish_type")


class DishDetailView(generic.DetailView):
    model = Dish


class CookDetailView(generic.DetailView):
    model = Cook


class DishTypeDetailView(generic.DetailView):
    model = DishType