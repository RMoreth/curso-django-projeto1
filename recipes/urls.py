from django.urls import path
from . import views

# dominio/recipes/

app_name = 'recipes'

urlpatterns = [
    path("", views.home, name="home"),  # Home
    path("recipes/<int:id>/", views.recipe, name="recipe")
]
