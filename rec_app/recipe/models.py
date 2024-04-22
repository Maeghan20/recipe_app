from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=1000, blank=False)
    description = models.CharField(max_length=1000, blank=False)
    ingredients = models.TextField(blank=False)
    instructions = models.TextField(blank=False)
    prep_time = models.IntegerField()
    cook_time = models.IntegerField()
    servings = models.IntegerField()

    class Meta: 
        db_table= "recipe"


# Create your models here.
