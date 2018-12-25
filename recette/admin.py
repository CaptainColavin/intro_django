from django.contrib import admin
from .models import Ingredient, Recette, IngredientRecette

class IngredientAdmin(admin.TabularInline):
    model = IngredientRecette
    extra = 1

class RecetteAdmin(admin.ModelAdmin):
    inlines = [IngredientAdmin,]

# Register your models here.
admin.site.register(Ingredient)
admin.site.register(Recette, RecetteAdmin)
admin.site.register(IngredientRecette)
