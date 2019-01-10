from django.contrib import admin
from .models import Symptom, Diagnosis, Treatment, Location

class SymptomAdmin(admin.ModelAdmin):
    fields = ['symptom_text']

# Register models
admin.site.register(Symptom, SymptomAdmin)
admin.site.register(Diagnosis)
admin.site.register(Treatment)
admin.site.register(Location)
