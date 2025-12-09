

from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

import json,uuid

from .models import Note

# Seed 
@csrf_exempt
@require_http_methods(['GET'])
def execute_seed(request):
    image_url = "https://static.vecteezy.com/system/resources/previews/016/762/752/non_2x/note-book-supply-free-vector.jpg"
    notes = [] #objec1, object2, object3 ..... objectns
    
    # Delete all Notes 
    Note.objects.all().delete()
    
    # Generate Seed
    for i in range(100):
        notes.append(
            Note(
                id = uuid.uuid4(),
                nombre = f"Note {i}",
                descripcion = f"Description {i}",
                imagen = image_url,
                estado = "Pendiente",
                # status = True
            )
        )
        
    # Save Seed in the database
    Note.objects.bulk_create(notes)
    
    return JsonResponse({
             "message": "Seed executed successfully",
             "Amount of notes": len(notes)
           }, status=200)
    
    
def get_notes_list(request):
    # Obtener todas las notas con status = True 
    notes = Note.objects.filter(status=True)
    
    return render(request, 'notes/index.html', {'notes': notes})
    