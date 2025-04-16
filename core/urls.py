from django.urls import path

from core.views import (
    index,
    DishTypeListView,
    CookListView,
    DishListView,
    DishDetailView,
    CookDetailView
)


urlpatterns = [
    path("", index, name="index"),
    path(
        "dish-types/",
        DishTypeListView.as_view(),
        name="dish-type-list"
    ),

    path(
        "dishes/",
        DishListView.as_view(),
        name="dish-list"
    ),

    path(
        "cooks/",
        CookListView.as_view(),
        name="cook-list"
    ),

    path(
        "dishes/<int:pk>/",
        DishDetailView.as_view(),
        name="dish-detail"
    ),

path(
        "cooks/<int:pk>/",
        CookDetailView.as_view(),
        name="cook-detail"
    ),
]

app_name = "core"