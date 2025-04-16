from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView, UpdateView, DeleteView

from core.models import (
    DishType,
    Cook,
    Dish,
    Ingredient
)


@login_required
def index(request):
    num_cooks = Cook.objects.count()
    num_dishes = Dish.objects.count()
    num_dish_types = DishType.objects.count()
    num_ingredients = Ingredient.objects.count()
    context = {
        "num_cooks": num_cooks,
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
    paginate_by = 10


class IngredientListView(generic.ListView):
    model = Ingredient
    template_name = "core/ingredient_list.html"
    paginate_by = 10


class IngredientDetailView(generic.DetailView):
    model = Ingredient


class DishListView(generic.ListView):
    model = Dish
    queryset = Dish.objects.select_related("dish_type")
    paginate_by = 10


class DishDetailView(generic.DetailView):
    model = Dish


class CookDetailView(generic.DetailView):
    model = Cook


class DishTypeCreateView(generic.CreateView):
    model = DishType
    fields = ['name']


class DishTypeUpdateView(generic.UpdateView):
    model = DishType
    fields = ["name"]
    success_url = reverse_lazy("dish-type-list")


class DishTypeDeleteView(generic.DeleteView):
    model = DishType
    success_url = reverse_lazy("dish-type-list")


class IngredientCreateView(CreateView):
    model = Ingredient
    fields = ['name']
    template_name = "core/ingredient_form.html"
    success_url = reverse_lazy("core:ingredient-list")



class IngredientUpdateView(UpdateView):
    model = Ingredient
    fields = ['name']
    template_name = "core/ingredient_form.html"
    success_url = reverse_lazy("core:ingredient-list")


class IngredientDeleteView(DeleteView):
    model = Ingredient
    context_object_name = "ingredient"
    template_name = "core/ingredient_delete_confirm.html"
    success_url = reverse_lazy("core:ingredient-list")


class DishCreateView(CreateView):
    model = Dish
    fields = ["name", "description", "price", "dish_type", "cooks", "ingredients"]
    success_url = reverse_lazy("dish-list")


class DishUpdateView(UpdateView):
    model = Dish
    fields = ["name", "description", "price", "dish_type", "cooks", "ingredients"]
    success_url = reverse_lazy("dish-list")


class DishDeleteView(DeleteView):
    model = Dish
    success_url = reverse_lazy("dish-list")
