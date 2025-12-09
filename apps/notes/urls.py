
from django.urls import path
from . import views

urlpatterns = [
    path('seed/', views.execute_seed, name='execute_seed'),
    
    path('', views.get_notes_list, name='get_notes_list'),
]


# CREAMOS UN MODELO --> BACKEND --> ENDPOINT --> FRONTEND