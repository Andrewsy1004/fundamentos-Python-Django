from django.db import models

# Create your models here.

class Author(models.Model):
    name        = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    birth_date  = models.DateField(null=False)
    biography   = models.TextField(max_length=1000, null=True)
    age         = models.IntegerField(max_length=3, null=True)
    status      = models.BooleanField(default=True)
    