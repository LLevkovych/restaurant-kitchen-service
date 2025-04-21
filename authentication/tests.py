from django.test import TestCase
from django.urls import reverse
from core.models import Cook


class AuthenticationTests(TestCase):
    def setUp(self):
        self.credentials = {
            "username": "testcook",
            "password": "securepass123",
            "first_name": "John",
            "last_name": "Doe",
            "years_of_experience": 5,
        }
        self.cook = Cook.objects.create_user(**self.credentials)

        self.new_user_data = {
            "username": "newuser",
            "password1": "testpass123",
            "password2": "testpass123",
            "first_name": "Test",
            "last_name": "User",
            "years_of_experience": 5,
        }

    def test_register_view_get(self):
        response = self.client.get(reverse("authentication:register"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/register.html")

    def test_register_view_post(self):
        response = self.client.post(
            reverse("authentication:register"), self.new_user_data
        )

        if response.status_code != 302:
            print(response.context["form"].errors)
        self.assertEqual(response.status_code, 302)

    def test_login_logout_flow(self):
        login = self.client.post(
            reverse("authentication:login"), self.credentials
        )
        self.assertEqual(login.status_code, 302)

        profile = self.client.get(reverse("authentication:profile"))
        self.assertEqual(profile.status_code, 200)

        logout = self.client.post(reverse("authentication:logout"))
        self.assertEqual(logout.status_code, 302)

    def test_profile_view_requires_login(self):
        response = self.client.get(reverse("authentication:profile"))
        self.assertEqual(response.status_code, 302)

        self.client.login(**self.credentials)
        response = self.client.get(reverse("authentication:profile"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/profile.html")

    def test_profile_update(self):
        self.client.login(**self.credentials)
        update_data = {
            "first_name": "Updated",
            "last_name": "Name",
            "years_of_experience": 10,
        }
        response = self.client.post(
            reverse("authentication:profile-update"), update_data
        )
        self.assertEqual(response.status_code, 302)

        self.cook.refresh_from_db()
        self.assertEqual(self.cook.first_name, "Updated")
        self.assertEqual(self.cook.years_of_experience, 10)

    def test_change_password(self):
        self.client.login(**self.credentials)
        data = {
            "old_password": "securepass123",
            "new_password1": "NewSecret456!",
            "new_password2": "NewSecret456!",
        }
        response = (self.client.post
                    (reverse("authentication:change-password"), data)
                    )
        self.assertEqual(response.status_code, 302)

        self.client.logout()
        login_old = self.client.login(
            username="testcook",
            password="securepass123"
        )
        self.assertFalse(login_old)

        login_new = self.client.login(
            username="testcook",
            password="NewSecret456!"
        )
        self.assertTrue(login_new)
