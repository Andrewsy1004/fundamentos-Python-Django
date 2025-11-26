# Listas, Tuplas, Diccionarios, Conjuntos

# Listas 
mis_pagos = [1000, 2000, 3000, 4000]

mis_pagos.append(5000)
mis_pagos.remove(2000)
print(mis_pagos[1])

for pago in mis_pagos:
    print(pago)

for index, pago in enumerate(mis_pagos):
    print(f'index {index} pago {pago}')

# Tuplas 
puntos_geograficos = (10, 20)

# puntos_geograficos.append(30)  # Warning --> No se puede agregar, son no mutables

print(puntos_geograficos[0])
print(puntos_geograficos[1])

for punto in puntos_geograficos:
    print(punto)


# Diccionarios (JSON -> JavaScript Object Notation)
personas = [
    {
        'id': 1,
        'name': 'Juan2 Doe',
        'edad': 30
    },
    {
        'id': 2,
        'name': 'Jane Doe',
        'edad': 25
    },
    {
        'id': 3,
        'name': 'John Doe',
        'edad': 30
    }
]

# Agregar un elemento
personas.append({
    'id': 4,
    'name': 'Andressss Doe',
    'edad': 30
})

# Eliminar un elemento
personas.remove(personas[0])

# Recorrer un Diccionario
print("\n Recorrer un Diccionario")
for persona in personas:
    print(persona['name'])
    

# Conjuntos
print("\n Conjuntos")
conjunto_A = {1,2,3,4,5,6,6,6,6,6,66,6,6}
conjunto_B = {4,5,6,7,8,9}

print(conjunto_A)

# Unir dos conjuntos
conjunto_C = conjunto_A.union(conjunto_B)
print(conjunto_C)

# Intersección de dos conjuntos
conjunto_D = conjunto_A.intersection(conjunto_B)
print(conjunto_D)
