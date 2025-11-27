from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

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