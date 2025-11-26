

try:
     numero = int(input("Ingrese un número: "))
     print("El número ingresado es:", numero)
     print(f"El número ingresado es: {numero}")
except ValueError as e:
    print(f"Debes, ingresar un número y no un caracter: {e}")
finally:
    print("Fin del programa")
    
# Manejar las division de cero
numero_a = int(input("Ingrese un número: "))
numero_b = int(input("Ingrese otro número: "))

try:
    print(f"El resultado es: {numero_a / numero_b}")
except ZeroDivisionError as e:
    print(f"No se puede dividir por cero: {e}")
    
# Mayor de edad, con el fin de entrar a la discteca 


# try:
    #  edad < 0 
    # if edad < 0:
    #     raise Exception("La edad no puede ser negativa") 
    
    # if edad >= 18:
    #     print("Usted es mayor de edad")
    # else:
    #     print("Usted es menor de edad")
# except Exception as e:
#     print(f"Hubo un error: {e}")

print("\nManejo de excepciones, personalizadas")
try:
    edad = -10
    if edad < 0:
        raise Exception("La edad no puede ser negativa")
except Exception as e:
    print("Error:", e)

