class persona:    
    def __init__(self, nombre, apellido, edad):
        
        # Validaciones, edad no sea negativa
        if edad < 0:
            raise Exception("La edad no puede ser negativa")
         
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad
    
    # Getters
    def get_nombre(self):
        return self.__nombre
    
    def get_apellido(self):
        return self.__apellido
    
    def get_edad(self):
        return self.__edad
    
    # Setters
    def set_nombre(self, nombre):
        self.__nombre = nombre
        
    def set_apellido(self, apellido):
        self.__apellido = apellido
        
    def set_edad(self, edad):
        if edad < 0:
            raise Exception("La edad no puede ser negativa")
        self.__edad = edad
        
        
# Instancia de la clase persona
persona1 = persona("Diego", "García", 20)
print(persona1.get_nombre())

persona1.set_edad(-20)


