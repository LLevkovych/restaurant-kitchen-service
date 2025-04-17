from django.urls import path, reverse_lazy
from authentication import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="registration/login.html",
            next_page=reverse_lazy("authentication:profile"),  # <-- це важливо
        ),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(
            next_page=reverse_lazy("authentication:login")
        ),
        name="logout",
    ),
    path(
        "register/",
        views.CookRegisterView.as_view(),
        name="register"
    ),
    path(
        "profile/",
        views.ProfileView.as_view(),
        name="profile"
    ),
    path(
        "change-password/",
        views.ChangePasswordView.as_view(),
        name="change-password"
    ),
    path(
        "profile/update/",
        views.profile_update,
        name="profile-update"
    ),
]

app_name = "authentication"
