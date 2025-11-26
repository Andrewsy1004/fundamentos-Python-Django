
# Ejemplo de herencia, aninameles ( nombre, edad) y clases hijas perro y gato sonido que hacen 

# classmethod y staticmethod

class Animal:
    def __init__(self, nombre, edad):
        
        # Validaciones
        if edad < 0:
            raise Exception("La edad no puede ser negativa")
        
        if nombre == "":
            raise Exception("El nombre no puede ser vacio")
        
        self.__nombre = nombre
        self.__edad = edad
        
    #  getter
    def get_nombre(self):
        return self.__nombre
    
    def get_edad(self):
        return self.__edad
    
    # setter
    def set_nombre(self, nombre):
        self.__nombre = nombre
        
    def set_edad(self, edad):
        self.__edad = edad
        
    def sonido(self):
     pass
        
class Perro(Animal):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
        
    def sonido(self):
        return "Guau guau"
    
    @staticmethod
    def saludar():
        return "Guau guau"

class Gato(Animal):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
        
    def sonido(self):
        return "Miau miau"
    
# Instacnias 
perro_pipul = Perro("Pipul", 3)
gato_michi = Gato("Michi", 2)

print(f"Yo soy un perro y hago el sonido {perro_pipul.sonido()}")
print(f"Yo soy un gato y hago el sonido {gato_michi.sonido()}")

print(Perro.saludar())