from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from authentication.models import Cook
from core.models import DishType, Dish, Ingredient


def index(request):
    num_cooks = Cook.objects.count()
    num_dishes = Dish.objects.count()
    num_dish_types = DishType.objects.count()
    context = {
        "num_cooks": num_cooks,
        "num_dishes": num_dishes,
        "num_dish_types": num_dish_types,
    }
    return render(request, "core/index.html", context=context)


class CookListView(LoginRequiredMixin, generic.ListView):
    model = Cook
    paginate_by = 10
    template_name = "core/cook_list.html"
    context_object_name = "cook_list"

    def get_queryset(self):
        query = self.request.GET.get("query", "")
        queryset = Cook.objects.all()
        if query:
            queryset = queryset.filter(
                Q(username__icontains=query) |
                Q(first_name__icontains=query) |
                Q(last_name__icontains=query)
            )
        return queryset


class CookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cook
    template_name = "core/cook_detail.html"
    context_object_name = "cook"


class DishTypeListView(generic.ListView):
    model = DishType
    template_name = "core/dish_type_list.html"
    context_object_name = "dish_type_list"
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get("query", "")
        queryset = DishType.objects.all()
        if query:
            queryset = queryset.filter(Q(name__icontains=query))
        return queryset


class IngredientListView(generic.ListView):
    model = Ingredient
    template_name = "core/ingredient_list.html"
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get("query", "")
        queryset = Ingredient.objects.all()
        if query:
            queryset = queryset.filter(name__icontains=query)
        return queryset


class IngredientDetailView(generic.DetailView):
    model = Ingredient


class DishListView(generic.ListView):
    model = Dish
    queryset = Dish.objects.select_related("dish_type")
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get("query", "")
        queryset = Dish.objects.all()
        if query:
            queryset = queryset.filter(
                Q(name__icontains=query) | Q(description__icontains=query)
            )
        return queryset


class DishDetailView(generic.DetailView):
    model = Dish


class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = DishType
    fields = ["name"]
    template_name = "core/dish_type_form.html"
    success_url = reverse_lazy("core:dish-type-list")


class DishTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = DishType
    fields = ["name"]
    template_name = "core/dish_type_form.html"
    success_url = reverse_lazy("core:dish-type-list")


class DishTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DishType
    template_name = "core/dish_type_confirm_delete.html"
    success_url = reverse_lazy("core:dish-type-list")


class IngredientCreateView(LoginRequiredMixin, generic.CreateView):
    model = Ingredient
    fields = ["name"]
    template_name = "core/ingredient_form.html"
    success_url = reverse_lazy("core:ingredient-list")


class IngredientUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Ingredient
    fields = ["name"]
    template_name = "core/ingredient_form.html"
    success_url = reverse_lazy("core:ingredient-list")


class IngredientDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Ingredient
    context_object_name = "ingredient"
    template_name = "core/ingredient_delete_confirm.html"
    success_url = reverse_lazy("core:ingredient-list")


class DishCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dish
    fields = [
        "name",
        "description",
        "price",
        "dish_type",
        "cooks",
        "ingredients"
    ]
    template_name = "core/dish_form.html"
    success_url = reverse_lazy("core:dish-list")


class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    fields = [
        "name",
        "description",
        "price",
        "dish_type",
        "cooks",
        "ingredients"
    ]
    template_name = "core/dish_form.html"
    success_url = reverse_lazy("core:dish-list")


class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    template_name = "core/dish_confirm_delete.html"
    success_url = reverse_lazy("core:dish-list")
