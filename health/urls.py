from django.urls import path

from . import views

app_name = 'health'
urlpatterns = [
    path('', views.home, name='home'),
    path('<int:symptom_id>/', views.diagnoses, name='diagnoses'),
    # path('<int:diagnosis_id>/treatment/', views.treatment, name='treatment')
]
