from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from organization.models import User

class UserDetailView(LoginRequiredMixin, generic.DeleteView):
    model = User
    template_name = "organization/user_detail.html"
    context_object_name = "user"

class UserCreateView(LoginRequiredMixin, generic.CreateView):
    model = User
    template_name = "organization/user_form.html"
    fields = ["username", "email", "phone_number", "city", "password"]
    success_url = reverse_lazy("user-list")

class UserUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = User
    template_name = "organization/user_form.html"
    fields = ["username", "email", "phone_number", "city"]
    success_url = reverse_lazy("user-list")

class UserDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = User
    template_name = "organization/user_confirm_delete.html"
    success_url = reverse_lazy("user-list")
