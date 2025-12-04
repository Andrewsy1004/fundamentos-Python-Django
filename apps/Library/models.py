from django.db import models

# Create your models here.

class Author(models.Model):
    name        = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    birth_date  = models.DateField(null=False)
    biography   = models.TextField(max_length=1000, null=True)
    age         = models.IntegerField(max_length=3, null=True)
    status      = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
class Book(models.Model):
    title            = models.CharField(max_length=100)
    publication_date = models.DateField(null=False)
    pages            = models.IntegerField(max_length=10)
    isbn             = models.CharField(max_length=50)
    status           = models.BooleanField(default=True)
    
    # relaciones 
    author = models.ForeignKey( Author, on_delete=models.CASCADE, related_name="books" )
    
    def __str__(self):
        return self.title