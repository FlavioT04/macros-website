from django.db import models

class Food_display(models.Model):
    food_name = models.CharField(max_length=30)
    f_protein = models.DecimalField(max_digits=5, decimal_places=2)
    f_carbs = models.DecimalField(max_digits=5, decimal_places=2)
    f_fat = models.DecimalField(max_digits=5, decimal_places=2)
    f_calories = models.DecimalField(max_digits=6, decimal_places=2) # Use method compute calories

    def add_food():
        pass

class Stats(models.Model):
    food_id = models.ForeignKey(Food_display, on_delete=models.CASCADE)
    total_protein = models.DecimalField(max_digits=5, decimal_places=2)
    total_carbs = models.DecimalField(max_digits=5, decimal_places=2)
    total_fat = models.DecimalField(max_digits=5, decimal_places=2)
    total_calories = models.DecimalField(max_digits=6, decimal_places=2) # Use method compute calories

# Calculates calories in food
def compute_calories(protein, carbs, fat):
    return protein*4 + carbs*4 + fat*9
