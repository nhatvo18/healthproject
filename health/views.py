from django.http import HttpResponse, Http404
from django.shortcuts import render

from .models import Symptom, Diagnosis

# Home page
def home(request):
    common_symptoms = Symptom.objects.all()[:5]
    context = { 'common_symptoms': common_symptoms }
    return render(request, 'health/home.html', context)

# Diagnoses page
def diagnoses(request, symptom):
    # Check if symptom exists in database
    try:
        s = Symptom.objects.get(symptom_text=symptom)
    except Symptom.DoesNotExist:
        raise Http404("Symptom does not exist in system.")
    context = { 's': s }
    return render(request, 'health/diagnoses.html', context)

# Treatment page
def treatment(request, diagnosis):
    # Check if diagnosis exists in database
    try:
        d = Diagnosis.objects.get(diagnosis_text=diagnosis)
    except Diagnosis.DoesNotExist:
        raise Http404("Diagnosis does not exist in system.")
    context = { 'd': d }
    return render(request, 'health/treatment.html', context)

# Generate a case
def case(request):
    return render(request, 'health/case.html')
