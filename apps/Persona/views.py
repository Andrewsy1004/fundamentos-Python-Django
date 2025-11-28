from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

# Simulando una base de datos
personas = [
    {
        'id': 1,
        'name': 'Javier',
        'last_name': 'Gonzalez',
        'age': 23
    },
    {
        'id': 2,
        'name': 'Fernando',
        'last_name': 'Gonzalez',
        'age': 23
    },
    {
        'id': 3,
        'name': 'Fernando',
        'last_name': 'Gonzalez',
        'age': 23
    },
    {
        'id': 4,
        'name': 'Fernando',
        'last_name': 'Gonzalez',
        'age': 23
    }
]

# Vistas
def get_all_people(request):
    return JsonResponse(personas, safe=False)

def get_person_by_id(request, id):
    personab = None
    
    for persona in personas:
        if persona['id'] == id:
            personab = persona
            break
        else:
            personab = None
     
    if personab == None:
        return JsonResponse({'message': 'Persona no encontrada'}, status=404)       
    
    return JsonResponse(personab, safe=False)


# renderizar html
def hello_world_html(request, name):
    return HttpResponse(f"<h1>Hello {name} !!</h1>")

@csrf_exempt
def create_person(request):
    if request.method != 'POST':
        return JsonResponse({'message': 'Persona creada'}, status=201)
    
    data = json.loads(request.body)
    
    # Validations
    if data.get("name") is None:
        return JsonResponse({"error": "El campo name es obligatorio"}, status=400)
    
    if data.get("last_name") is None:
        return JsonResponse({"error": "El campo last_name es obligatorio"}, status=400)
    
    if data.get("age") is None:
        return JsonResponse({"error": "El campo age es obligatorio"}, status=400)

    
    persona = {
        'id': len(personas) + 1,
        'name': data.get('name'),
        'last_name': data.get('last_name'),
        'age': data.get('age')
    }
    
    personas.append(persona)
    
    return JsonResponse(persona, safe=False)


@csrf_exempt
def delete_person(request, id):
    if request.method != 'DELETE':
        return JsonResponse({'message': 'Persona eliminada'}, status=204)
    
    # Validations
    if id is None:
        return JsonResponse({"error": "El campo id es obligatorio"}, status=400)
    
    # for persona in personas:
    #     if persona['id'] == id:
    #         personas.remove(persona)
    #         return JsonResponse({'message': 'Persona eliminada'}, status=204)
    
    persona = next((persona for persona in personas if persona['id'] == id), None)
    
    if persona is not None:
        personas.remove(persona)
        return JsonResponse({'message': 'Persona eliminada'}, status=204)
    
    return JsonResponse({'message': 'Persona no encontrada'}, status=404)

@csrf_exempt
def update_person(request, id):
    if request.method != 'PATCH':
        return JsonResponse({'message': 'Metodo no permitido'}, status=405)
    
    # 1. encontrar la personas del id
    persona = next((P for P in personas if P['id'] == id), None)
    
    if persona is None:
        return JsonResponse({'message': 'Persona no encontrada'}, status=404)
    
    data = json.loads(request.body)
    
    if data.get('name') is not None:
        persona['name'] = data.get('name')
        #  aaaa          = bbbbb
    
    if data.get('last_name') is not None:
        persona['last_name'] = data.get('last_name')
    
    if data.get('age') is not None:
        persona['age'] = data.get('age')
    
    return JsonResponse({'message': 'Persona actualizada', 'persona': persona}, safe=False)


# html, mostrar todos los usuarios, archivo index.html 
def show_all_users(request):
    return render(request, 'Persona/index.html', {'personas': personas,'role':"usuario", "name":"Juan"})

def show_information_by_id(request, id):
    
    # find the user with the id
    person_to_search = next((P for P in personas if P['id'] == id), None)
    
    # if not found
    if person_to_search is None:
       return HttpResponse(f"Usuario con id {id} no encontrado")
    
    return render(request, 'Persona/personalInformation.html', {'person': person_to_search})