from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse

import json

from .models import Author

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
    