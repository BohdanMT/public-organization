from django.urls import path

from organization.views.views import index

urlpatterns = [
    path("", index, name="index"),
]

app_name = "organization"