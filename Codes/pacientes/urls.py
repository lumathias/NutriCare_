from django.urls import path
from . import views

app_name = 'patients'

urlpatterns = [
    path('<int:patient_id>/', views.patient_detail, name='patient_detail'),
]
