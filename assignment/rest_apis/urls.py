from django.urls import path
from . import views

urlpatterns = [
    # api
    path('v1/', views.validate_numeric_entity,name='validate_numeric_entity'),
    path('v2/', views.validate_finite_values_entity,name='validate_finite_values_entity')
]