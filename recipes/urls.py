from django.urls import path
from . import views

# dominio/recipes/

app_name = 'recipes'

urlpatterns = [
    path("", views.home, name="home"),  # Home
    path("recipes/search/", views.search, name="search"),
    path("recipes/<int:id>/", views.recipe, name="recipe"),
    path("recipes/category/<int:category_id>/",
         views.category, name="category"),

]
