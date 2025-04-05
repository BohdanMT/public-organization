from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from organization.models import City


class CityListView(LoginRequiredMixin, generic.ListView):
    model = City
    template_name = "organization/city_list.html"
    context_object_name = "cities"


class CityCreateView(LoginRequiredMixin, generic.CreateView):
    model = City
    template_name = "organization/city_form.html"
    fields = ["name", "region", "district", "starostat", "head_of_starostat"]
    success_url = reverse_lazy("city-list")


class CityUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = City
    template_name = "organization/city_form.html"
    fields = ["name", "region", "district", "starostat", "head_of_starostat"]
    success_url = reverse_lazy("city-list")


class CityDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = City
    template_name = "organization/city_confirm_delete.html"
    success_url = reverse_lazy("city-list")