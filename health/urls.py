from django.urls import path

from . import views

app_name = 'health'
urlpatterns = [
    path('', views.home, name='home'),
    path('case/', views.case, name='case'),
    path('<str:symptom>/', views.diagnoses, name='diagnoses'),
    path('<str:diagnosis>/treatment/', views.treatment, name='treatment'),
     # Copied from docs; need review below:
    path('test/formwizard/', views.ContactWizard.as_view(views.ContactWizard.form_list), name='formwizard'),
]
