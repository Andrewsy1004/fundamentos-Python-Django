

from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseBadRequest

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
    for i in range(10):
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



@csrf_exempt
def create_note(request):
    try:
        data = json.loads(request.body)
        
        # Validate data
        required_fields = ['name', 'description', 'image', 'state']
        
        for field in required_fields:
            if field not in data:
                return JsonResponse({"error": f"Missing field: {field}"}, status=400)    
    
        # Create Instance
        note = Note(
            id = uuid.uuid4(),
            nombre = data.get('name'),
            descripcion = data.get('description'),
            imagen = data.get('image'),
            estado = data.get('state'),
        )
        
        # Save in the database
        note.save()
        
        return JsonResponse({"message": "Note created successfully"}, status=201)
    
    except Exception as e:
        return HttpResponseBadRequest({"error": str(e)})


@csrf_exempt
@require_http_methods(['GET'])
def execute_seed(request):
    image_url = "https://static.vecteezy.com/system/resources/previews/016/762/752/non_2x/note-book-supply-free-vector.jpg"
    notes = []
    
    Note.objects.all().delete()
    
    for i in range(10):
        notes.append(
            Note(
                id = uuid.uuid4(),
                nombre = f"Note {i}",
                descripcion = f"Description {i}",
                imagen = image_url,
                estado = "pendiente",
            )
        )
        
    Note.objects.bulk_create(notes)
    
    return JsonResponse({
        "message": "Seed executed successfully",
        "Amount of notes": len(notes)
    }, status=200)
    

def get_notes_list(request):
    notes = Note.objects.filter(status=True)
    return render(request, 'notes/index.html', {'notes': notes})


@csrf_exempt
@require_http_methods(['POST'])
def create_note(request):
    try:
        data = json.loads(request.body)
        
        required_fields = ['name', 'description', 'image', 'state']
        
        for field in required_fields:
            if field not in data:
                return JsonResponse({"error": f"Missing field: {field}"}, status=400)    
    
        note = Note(
            id = uuid.uuid4(),
            nombre = data.get('name'),
            descripcion = data.get('description'),
            imagen = data.get('image'),
            estado = data.get('state'),
        )
        
        note.save()
        
        return JsonResponse({"message": "Note created successfully"}, status=201)
    
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)


@csrf_exempt
@require_http_methods(['GET'])
def get_note_by_id(request, note_id):
    try:
        note = Note.objects.get(id=note_id, status=True)
        
        return JsonResponse({
            "id": str(note.id),
            "nombre": note.nombre,
            "descripcion": note.descripcion,
            "imagen": note.imagen,
            "estado": note.estado,
            "created_at": note.created_at.strftime("%d/%m/%Y %H:%M"),
        }, status=200)
        
    except Note.DoesNotExist:
        return JsonResponse({"error": "Note not found"}, status=404)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


@csrf_exempt
@require_http_methods(['PUT'])
def update_note_by_id(request, note_id):
    try:
        note = Note.objects.get(id=note_id, status=True)
        data = json.loads(request.body)
        
        if 'name' in data:
            note.nombre = data.get('name')
        
        if 'description' in data:
            note.descripcion = data.get('description')
        
        if 'image' in data:
            note.imagen = data.get('image')
        
        if 'state' in data:
            note.estado = data.get('state')
        
        note.save()
        
        return JsonResponse({"message": "Note updated successfully"}, status=200)
        
    except Note.DoesNotExist:
        return JsonResponse({"error": "Note not found"}, status=404)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


@csrf_exempt
@require_http_methods(['DELETE'])
def delete_note_by_id(request, note_id):
    try:
        note = Note.objects.get(id=note_id, status=True)
        
        note.status = False
        note.save()
        
        return JsonResponse({"message": "Note deleted successfully"}, status=200)
        
    except Note.DoesNotExist:
        return JsonResponse({"error": "Note not found"}, status=404)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)