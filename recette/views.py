from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.forms import ModelForm
from .models import Recette,Ingredient , IngredientRecette
# Create your views here.
def index(request):
    return render(request, 'recette/index.html')

class RecetteForm(ModelForm):
    class Meta:
        model = Recette
        fields = '__all__'


def recette_list(request):
    recettes = Recette.objects.all()
    return render(request, 'recette/recettes.html', {'recettes': recettes})

def recette(request, id):
    recette = Recette.objects.get(id=id)
    ingredientsrecette = IngredientRecette.objects.filter(recette_id=id)
    return render(request, 'recette/recette.html', {'recette': recette, 'ingredientsrecette': ingredientsrecette})

def create_recette(request):
    if request.POST:
        form = RecetteForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['user']
            recette_nom = form.cleaned_data['nom']
            recette_duree = form.cleaned_data['duree']
            recette_parts = form.cleaned_data['nb_parts']
            instance = Recette.objects.create(user_id=username.id, nom=recette_nom, duree=recette_duree, nb_parts=recette_parts )

            for ingredient in form.cleaned_data['ingredients']:
                IngredientRecette.objects.create(ingredient=ingredient, recette=instance, quantite=10)
            return redirect('recettes')
    else:
        form = RecetteForm()
    return render(request, 'recette/create_recette.html', {'form': form})

def update_recette(request, id):
    recette = get_object_or_404(Recette, id=id)
    form = RecetteForm(request.POST or None, instance=recette)
    if form.is_valid():
        username = form.cleaned_data['user']
        recette_nom = form.cleaned_data['nom']
        recette_duree = form.cleaned_data['duree']
        recette_parts = form.cleaned_data['nb_parts']
        Recette.objects.filter(id=id).update(nom=recette_nom, duree=recette_duree, nb_parts=recette_parts)

        return redirect('recettes')
    return render(request, "recette/create_recette.html", {'form': form})



def delete_recette(request, id):
    recette = Recette.objects.get(id=id)
    recette.delete()
    return redirect('recettes')
