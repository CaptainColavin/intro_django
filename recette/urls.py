from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('recettes/',views.recette_list, name="recettes"),
    path('recettes/<int:id>',views.recette, name="recette"),
    path('recettes/create/',views.create_recette, name="createrecette"),
    path('recettes/update/<int:id>',views.update_recette, name="updaterecette"),
    path('recettes/delete/<int:id>',views.delete_recette, name="deleterecette"),
]
