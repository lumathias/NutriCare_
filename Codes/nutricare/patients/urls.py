from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'patients'

urlpatterns = [
    path('<int:patient_id>/', views.patient_detail, name='patient_detail'),
    path('<int:patient_id>/add_meal/', views.add_meal, name='add_meal'),
    path('<int:patient_id>/', views.patient_detail, name='patient_detail'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
