
from django.urls import path
from . import views

urlpatterns = [
    path('people', views.get_all_people, name='get_all_people'),
    path('people/<int:id>', views.get_person_by_id, name='get_person_by_id'),
    
    
    # renderizar html 
    path("hello/<str:name>", views.hello_world_html, name="hello_world_html"),
]