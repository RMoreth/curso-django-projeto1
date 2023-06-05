from django.urls import path
from . import views

# dominio/recipes/
urlpatterns = [
    path("", views.home),  # Home
    path("recipes/<int:id>/", views.recipe)
]
