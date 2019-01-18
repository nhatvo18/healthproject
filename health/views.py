from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from formtools.wizard.views import SessionWizardView

import random

from .models import Symptom, Diagnosis
from . import forms

# FORMS = [("address", myapp.forms.AddressForm),
#          ("paytype", myapp.forms.PaymentChoiceForm),
#          ("cc", myapp.forms.CreditCardForm),
#          ("confirmation", myapp.forms.OrderForm)]
#
# TEMPLATES = {"address": "checkout/billingaddress.html",
#              "paytype": "checkout/paymentmethod.html",
#              "cc": "checkout/creditcard.html",
#              "confirmation": "checkout/confirmation.html"}

# Home page
def home(request):
    common_symptoms = Symptom.objects.all()[:5]
    context = { 'common_symptoms': common_symptoms }
    return render(request, 'health/home.html', context)

class ContactWizard(SessionWizardView):
    form_list = [forms.ContactForm1, forms.ContactForm2]
    def done(self, form_list, form_dict, **kwargs):
        # Do something here
        return HttpResponseRedirect('health/test.html')

# Diagnoses page
def diagnoses(request, symptom):
    # Check if symptom exists in database
    try:
        s = Symptom.objects.get(symptom_text__icontains=symptom)
    except Symptom.DoesNotExist:
        raise Http404("Symptom does not exist in system.")
    except Symptom.MultipleObjectsReturned:
        return many_symptoms_found(request, symptom)
    context = { 's': s }
    return render(request, 'health/diagnoses.html', context)
    # return HttpResponse('Diagnosis page')

# If search returns many symptoms
def many_symptoms_found(request, symptom):
    try:
        s = Symptom.objects.filter(symptom_text__icontains=symptom)
    except Symptom.DoesNotExist:
        raise Http404("Cannot find any symptoms.")
    return render(request, 'health/search_suggest.html', { 's': s })

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
# Pick a random diagnosis, then pick 5 random symptoms
# of that diagnosis
def case(request):
    try:
        all_diagnoses = Diagnosis.objects.all()
    except all_diagnoses.DoesNotExist:
        raise Http404("Database is empty.")
    random_diagnosis = random.choice(all_diagnoses)
    symptoms = random_diagnosis.symptoms.all()
    random_symtoms = random.sample(list(symptoms), min(5, len(list(symptoms))))
    return render(request, 'health/case.html', { 'random_symtoms': random_symtoms })
