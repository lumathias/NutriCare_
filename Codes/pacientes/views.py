from django.shortcuts import render, get_object_or_404
from .models import Patient, Meal

def patient_detail(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    meals = Meal.objects.filter(patient=patient)
    return render(request, 'patients/patient_detail.html', {'patient': patient, 'meals': meals})

