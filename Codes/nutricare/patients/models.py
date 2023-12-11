from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)
    height = models.FloatField()
    weight = models.FloatField()
    plan = models.TextField()

class Meal(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    calories = models.FloatField()

    def __str__(self):
        return self.name
