from django import forms

class first_symptom(forms.Form):
    symptom1 = forms.CharField(max_length=200)

class second_symptom(forms.Form):
    symptom2 = forms.CharField(max_length=200)

class third_symptom(forms.Form):
    symptom3 = forms.CharField(max_length=200)
