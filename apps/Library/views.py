from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse

import json

from .models import Author, Book

# Create your views here.

@csrf_exempt
@require_http_methods(["POST"])
def create_author(request):
    data = json.loads(request.body)
    
    # if data.get("name") is None:
    #     return JsonResponse({"error": "El campo name es obligatorio"}, status=400)
    
    # if data.get("nationality") is None:
    #     return JsonResponse({"error": "El campo name es obligatorio"}, status=400)
        
    # if data.get("birth_date") is None:
    #     return JsonResponse({"error": "El campo birth_date es obligatorio"}, status=400)
        
    # if data.get("biography") is None:
    #     return JsonResponse({"error": "El campo biography es obligatorio"}, status=400)
    
    # if data.get("age") is None:
    #     return JsonResponse({"error": "El campo status es obligatorio"}, status=400)
    
    # Better way to validate required fields
    required_fields = ["name", "nationality", "birth_date", "biography", "age"]
    
    for field in required_fields:
        if data.get(field) is None:
            return JsonResponse({"error": f"El campo {field} es obligatorio"}, status=400)
    
    author = Author(
        name = data.get("name"),
        nationality = data.get("nationality"),
        birth_date = data.get("birth_date"),
        biography = data.get("biography"),
        age = data.get("age"),
    )
    
    author.save()
    
    return JsonResponse({
                          "message": "Autor creado", 
                          "author": {
                              "id": author.id,
                              "name": author.name,
                              "nationality": author.nationality,
                              "birth_date": author.birth_date,
                              "biography": author.biography,
                              "age": author.age,
                              "status": author.status
                          } 
                        }, status=201)
    

@csrf_exempt
@require_http_methods(["GET"])
def get_all_authors(request):
    # Obtener los usuarios los cuales tengan status = True
    
    authors = Author.objects.filter(status=True) # SELECT * FROM AUTHOR WHERE STATUS = True
    
    if authors is None:
        return JsonResponse({"message": "No se encontraron autores"}, status=404)
    
    return JsonResponse({"authors": list(authors.values())}, status=200)


@csrf_exempt
@require_http_methods(["GET"])
def get_user_by_id(request, id):
    author = Author.objects.filter(id=id, status=True).first()
    #  SELECT * FROM AUTHOR WHERE ID = id and STATUS = True
    
    if author is None:
        return JsonResponse({"message": "No se encontro el autor"}, status=404)
    
    return JsonResponse({ 
                         "author": {
                             "id": author.id,
                             "name": author.name,
                             "nationality": author.nationality,
                             "birth_date": author.birth_date,
                             "biography": author.biography,
                             "age": author.age,
                             "status": author.status
                         } 
                        }, status=200)
    
@csrf_exempt
@require_http_methods(["DELETE"])
def delete_autor_by_id(request, id):
    
    author = Author.objects.filter(id=id, status=True).first()
    
    if author is None:
        return JsonResponse({"message": "No se encontro el autor"}, status=404)
    
    author.status = False
    author.save()
    
    return JsonResponse({"message": "Autor eliminado"}, status=200)


@csrf_exempt
@require_http_methods(["PATCH"])
def update_author_by_id(request, id):
    
    #  Verificar si el autor existe y si esta activo en la base de datos
    autor_id = Author.objects.filter(id=id, status=True).first()
    
    if autor_id is None:
        return JsonResponse({"message": "No se encontro el autor"}, status=404)
    
    # Cargar los datos del body ( cliente )
    data = json.loads(request.body)
    
    if data.get("name") is not None:
        autor_id.name = data.get("name")
    
    if data.get("nationality") is not None:
        autor_id.nationality = data.get("nationality")
    
    if data.get("birth_date") is not None:
        autor_id.birth_date = data.get("birth_date")
    
    if data.get("biography") is not None:
        autor_id.biography = data.get("biography")
    
    if data.get("age") is not None:
        autor_id.age = data.get("age")
     
    # Hacer el update, en la base de datos   
    autor_id.save()
    
    return JsonResponse({ 
                         "message": "Autor actualizado",
                         "author": {
                             "id": autor_id.id,
                             "name": autor_id.name,
                             "nationality": autor_id.nationality,
                             "birth_date": autor_id.birth_date,
                             "biography": autor_id.biography,
                             "age": autor_id.age
                         }
                        }, status=200)


# endponts de libros


@csrf_exempt
@require_http_methods(["POST"])
def create_book(request):
    data = json.loads(request.body)
    
    id_user = data.get("id_user")
    
    # verificiar si el usuario existe y esta activo en la bd
    user = Author.objects.filter(id=id_user, status=True).first()
    
    if user is None:
        return JsonResponse({"message": "No se encontro el autor"}, status=404)
    
    for field in ["title", "publication_date", "pages", "isbn"]:
        if data.get(field) is None:
            return JsonResponse({"error": f"El campo {field} es obligatorio"}, status=400)
    
    # Crear el libro, instanciando la clase 
    book = Book(
        title = data.get("title"),
        publication_date = data.get("publication_date"),
        pages = data.get("pages"),
        isbn = data.get("isbn"),
        status = True,
        author = user
    )
    
    # Guardar el libro, en la bd
    book.save()
    
    return JsonResponse({
         "message": "Libro creado",
         "book": {
             "id": book.id,
             "title": book.title,
             "publication_date": book.publication_date,
             "pages": book.pages,
             "isbn": book.isbn,
             "status": book.status,
             "author": {
                 "id": book.author.id,
                 "name": book.author.name,
                 "nationality": book.author.nationality,
                 "birth_date": book.author.birth_date,
                 "biography": book.author.biography,
                 "age": book.author.age
             }
         }
    }, status=201)
    

@csrf_exempt
@require_http_methods(["GET"])
def get_book_by_id(request, id):
    
    book_found = Book.objects.filter(id=id, status=True).first()
    
    if book_found is None:
        return JsonResponse({"message": "No se encontro el libro"}, status=404)
    
    return JsonResponse({
        "book": {
            "id": book_found.id,
            "title": book_found.title,
            "publication_date": book_found.publication_date,
            "pages": book_found.pages,
            "isbn": book_found.isbn,
            "name_author": book_found.author.name
        }
    })
    
   
