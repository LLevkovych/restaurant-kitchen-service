from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import UpdateView

from authentication.forms import CookCreationForm, ProfileUpdateForm
from authentication.models import Cook


class CookRegisterView(generic.CreateView):
    form_class = CookCreationForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("authentication:login")


class ProfileView(LoginRequiredMixin, generic.TemplateView):
    template_name = "registration/profile.html"


class ChangePasswordView(LoginRequiredMixin, PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = "registration/change_password.html"
    success_url = reverse_lazy("authentication:profile")


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Cook
    form_class = ProfileUpdateForm
    template_name = "registration/profile_update.html"
    success_url = reverse_lazy("authentication:profile")

    def get_object(self, queryset=None):
        return self.request.user
