
from django.db import models

import uuid

class Note(models.Model):
    ESTADOS = [
        ('Pendiente', 'Pendiente'),
        ('En_proceso', 'En proceso'),
        ('Completada', 'Completada')
    ]
    
    id          = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre      = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=500)
    imagen      = models.TextField(max_length=200, null=True, blank=True)
    estado      = models.CharField(max_length=20, choices=ESTADOS, default='Pendiente')
    status      = models.BooleanField(default=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nombre
