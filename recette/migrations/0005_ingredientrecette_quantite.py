# Generated by Django 2.1.4 on 2018-12-13 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recette', '0004_auto_20181212_1446'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredientrecette',
            name='quantite',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
    ]