from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from authentication.forms import CookCreationForm, ProfileUpdateForm


class CookRegisterView(generic.CreateView):
    form_class = CookCreationForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("login")


class ProfileView(generic.TemplateView):
    template_name = "registration/profile.html"


class ChangePasswordView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = "registration/change_password.html"
    success_url = reverse_lazy("authentication:profile")  # <--- ОНОВЛЕНО


def profile_update(request):
    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("authentication:profile")  # <--- ОНОВЛЕНО
    else:
        form = ProfileUpdateForm(instance=request.user)
    return render(
        request,
        "registration/profile_update.html",
        {"form": form}
    )
