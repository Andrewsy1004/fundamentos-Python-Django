from django.urls import path
from . import views

urlpatterns = [
    path('seed/', views.execute_seed, name='execute_seed'),
    path('', views.get_notes_list, name='get_notes_list'),
    
    path('create/', views.create_note, name='create_note'),
    path('get_nota_by_id/<uuid:note_id>/', views.get_note_by_id, name='get_note_by_id'),
    path('update/<uuid:note_id>/', views.update_note_by_id, name='update_note_by_id'),
    path('delete/<uuid:note_id>/', views.delete_note_by_id, name='delete_note_by_id'),
]