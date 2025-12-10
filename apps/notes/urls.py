
from django.urls import path
from . import views

urlpatterns = [
    path('seed/', views.execute_seed, name='execute_seed'),
    
    path('', views.get_notes_list, name='get_notes_list'),
    path('create/', views.create_note, name='create_note'), 
]


# CREAMOS UN MODELO --> BACKEND --> ENDPOINT --> FRONTEND