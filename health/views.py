from django.http import HttpResponse, Http404
from django.shortcuts import render

from .models import Symptom, Diagnosis
# Create your views here

# Home page
def home(request):
    common_symptoms = Symptom.objects.all()[:5]
    context = { 'common_symptoms': common_symptoms }
    return render(request, 'health/home.html' ,context)

# Diagnoses page
def diagnoses(request, symptom_id):
    # Check if symptom exists in database
    try:
        s = Symptom.objects.get(pk=symptom_id)
    except Symptom.DoesNotExist:
        raise Http404("Symptom does not exist in system.")
    context = { 's': s }
    return render(request, 'health/diagnoses.html', context)

# Treatment page
def treatment(request, diagnosis):
    # Check if diagnosis exists in database
    try:
        d = Diagnosis.objects.get(treatment_text=diagnosis)
    except Diagnosis.DoesNotExist:
        raise Http404("Diagnosis does not exist in system.")
    context = { 'd': d }
    return render(request, 'health/treatment.html', context)
