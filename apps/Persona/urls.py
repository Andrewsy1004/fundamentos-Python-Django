
from django.urls import path
from . import views

urlpatterns = [
    path('people', views.get_all_people, name='get_all_people'),
    path('people/<int:id>', views.get_person_by_id, name='get_person_by_id'),
    
    path('create_person', views.create_person, name='create_person'),
    path('delete_person/<int:id>', views.delete_person, name='delete_person'),
    path('update_person/<int:id>', views.update_person, name='update_person'),
    
    # renderizar html 
    path("hello/<str:name>", views.hello_world_html, name="hello_world_html"),
    path("show_all_users", views.show_all_users, name="show_all_users"),
    path("personal_information/<int:id>", views.show_information_by_id, name="personal_information"),
    
]   