from django.urls import reverse
from django.test import TestCase
from core.models import Cook, DishType, Dish, Ingredient


class DishTestCase(TestCase):

    def setUp(self):
        self.dish_type = DishType.objects.create(name="Main Dish")
        self.cook = Cook.objects.create_user(
            username="testcook",
            password="testpass",
            first_name="John",
            last_name="Doe"
        )
        self.ingredient = Ingredient.objects.create(name="Tomato")

    def test_dish_list_view(self):
        dish = Dish.objects.create(
            name="Spaghetti",
            description="Delicious pasta",
            price=12.99,
            dish_type=self.dish_type,
        )
        dish.cooks.add(self.cook)

        response = self.client.get(reverse("core:dish-list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, dish.name)

    def test_dish_list_view_with_query(self):
        dish = Dish.objects.create(
            name="Spaghetti",
            description="Delicious pasta",
            price=12.99,
            dish_type=self.dish_type,
        )
        dish.cooks.add(self.cook)

        response = self.client.get(
            reverse("core:dish-list") + "?query=Spaghetti"
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, dish.name)

    def test_dish_create_view(self):
        self.client.login(username="testcook", password="testpass")

        response = self.client.post(
            reverse("core:dish-create"),
            {
                "name": "New Dish",
                "description": "Delicious dish",
                "price": 19.99,
                "dish_type": self.dish_type.id,
                "cooks": [self.cook.id],
                "ingredients": [self.ingredient.id],
            },
        )

        if response.status_code == 200:
            print(response.context["form"].errors)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Dish.objects.count(), 1)
        self.assertEqual(Dish.objects.first().name, "New Dish")

    def test_dish_update_view(self):
        dish = Dish.objects.create(
            name="Spaghetti",
            description="Delicious pasta",
            price=12.99,
            dish_type=self.dish_type,
        )
        dish.cooks.add(self.cook)
        dish.ingredients.add(self.ingredient)

        self.client.login(username="testcook", password="testpass")

        response = self.client.post(
            reverse("core:dish-update", args=[dish.pk]),
            {
                "name": "Updated Spaghetti",
                "description": "Yummy pasta",
                "price": 15.99,
                "dish_type": self.dish_type.id,
                "cooks": [self.cook.id],
                "ingredients": [self.ingredient.id],
            },
        )

        self.assertEqual(response.status_code, 302)

        dish.refresh_from_db()
        self.assertEqual(dish.name, "Updated Spaghetti")

    def test_dish_delete_view(self):
        dish = Dish.objects.create(
            name="Spaghetti",
            description="Delicious pasta",
            price=12.99,
            dish_type=self.dish_type,
        )
        dish.cooks.add(self.cook)

        self.client.login(username="testcook", password="testpass")
        response = self.client.post(
            reverse("core:dish-delete", args=[dish.pk])
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Dish.objects.count(), 0)
