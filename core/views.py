from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from core.models import DishType, Cook, Dish, Ingredient


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


class DishTypeListView(generic.ListView):
    model = DishType
    template_name = "core/dish_type_list.html"
    context_object_name = "dish_type_list"
    paginate_by = 10

    def get_queryset(self):

        query = self.request.GET.get("query", "")
        if query:
            return DishType.objects.filter(Q(name__icontains=query))
        return DishType.objects.all() 


class CookListView(generic.ListView):
    model = Cook
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get("query", "")
        if query:
            return Cook.objects.filter(name__icontains=query)
        return Cook.objects.all()


class IngredientListView(generic.ListView):
    model = Ingredient
    template_name = "core/ingredient_list.html"
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get("query", "")
        if query:
            return Ingredient.objects.filter(name__icontains=query)
        return Ingredient.objects.all()


class IngredientDetailView(generic.DetailView):
    model = Ingredient


class DishListView(generic.ListView):
    model = Dish
    queryset = Dish.objects.select_related("dish_type")
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get("query", "")
        if query:
            return Dish.objects.filter(
                Q(name__icontains=query) | Q(description__icontains=query)
            )
        return Dish.objects.all()


class DishDetailView(generic.DetailView):
    model = Dish


class CookDetailView(generic.DetailView):
    model = Cook


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
    fields = ["name", "description", "price", "dish_type", "cooks", "ingredients"]
    template_name = "core/dish_form.html"
    success_url = reverse_lazy("core:dish-list")


class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    fields = ["name", "description", "price", "dish_type", "cooks", "ingredients"]
    template_name = "core/dish_form.html"
    success_url = reverse_lazy("core:dish-list")


class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    template_name = "core/dish_confirm_delete.html"
    success_url = reverse_lazy("core:dish-list")


class ChangePasswordView(LoginRequiredMixin, PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = "registration/change_password.html"
    success_url = reverse_lazy("authentication:profile")
