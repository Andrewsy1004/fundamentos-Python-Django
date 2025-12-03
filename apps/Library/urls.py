from django.urls import path
from . import views

urlpatterns = [
    path('create_author', views.create_author, name='create_author'),
    
    path('get_all_authors', views.get_all_authors, name='get_all_authors'),
    path('get_author_by_id/<int:id>', views.get_user_by_id, name='get_author_by_id'),
    
    path('delete_author/<int:id>', views.delete_autor_by_id, name='delete_author'),
   
]