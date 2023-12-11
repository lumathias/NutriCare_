from django import forms
from .models import Patient, Meal

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'height', 'weight', 'plan']

class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ['name', 'calories']