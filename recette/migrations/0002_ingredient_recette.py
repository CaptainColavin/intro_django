# Generated by Django 2.1.4 on 2018-12-12 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recette', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='recette',
            field=models.ManyToManyField(through='recette.IngredientRecette', to='recette.Recette'),
        ),
    ]