from django.shortcuts import redirect, render, get_object_or_404
from .models import Meal, Patient
from .forms import MealForm


def add_meal(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    meal_form = MealForm(request.POST or None)

    if request.method == 'POST' and meal_form.is_valid():
        new_meal = meal_form.save(commit=False)
        new_meal.patient = patient
        new_meal.save()
        return redirect('patients:patient_detail', patient_id=patient.id)

    return render(request, 'add_meal.html', {'patient': patient, 'meal_form': meal_form})


def patient_detail(request):
    return patient_detail(Patient)