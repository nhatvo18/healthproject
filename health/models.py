from django.db import models

# Create your models here.

class Symptom(models.Model):
    # Symptom
    symptom_text = models.CharField(max_length=200)

    def __str__(self):
        return self.symptom_text

    class Meta:
        ordering = ('symptom_text',)

class Diagnosis(models.Model):
    # Diagnosis
    diagnosis_text = models.CharField(max_length=200)
    # One diagnosis can link to many symptoms; one symptom can link to many diagnoses
    # i.e. many-to-many relationship
    symptoms = models.ManyToManyField(Symptom)

    def __str__(self):
        return self.diagnosis_text

    class Meta:
        ordering = ('diagnosis_text',)

class Treatment(models.Model):
    # Treatment
    treatment_text = models.CharField(max_length=2000)
    # One diagnosis can link to many treatments; one treatment can link to many diagnoses
    # i.e. many-to-many relationship
    diagnoses = models.ManyToManyField(Diagnosis)

    def __str__(self):
        return self.treatment_text

    class Meta:
        ordering = ('treatment_text',)
