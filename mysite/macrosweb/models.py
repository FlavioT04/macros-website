from django.db import models

class Food_display(models.Model):

    name = models.CharField(max_length=30)
    protein = models.DecimalField(max_digits=5, decimal_places=2)
    carbs = models.DecimalField(max_digits=5, decimal_places=2)
    fat = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name

    def add_food():
        pass