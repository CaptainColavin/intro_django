from django.db import models

class Recette(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    nom = models.CharField(max_length=50)
    duree = models.IntegerField()
    nb_parts = models.IntegerField()
    ingredients = models.ManyToManyField('Ingredient', through='IngredientRecette')

    def __str__(self):
        return self.nom

class Ingredient(models.Model):
    nom = models.CharField(max_length=50)

    def __str__(self):
        return self.nom

class IngredientRecette(models.Model):
    recette = models.ForeignKey('Recette', on_delete=models.CASCADE)
    ingredient = models.ForeignKey('Ingredient', on_delete=models.CASCADE)
    quantite = models.IntegerField()
    unite = models.CharField(max_length=50)
