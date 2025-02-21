estudiantes = [
    {"nombre": "Ana", "notas": [7, 8, 6]},
    {"nombre": "Luis", "notas": [4, 5, 3]},
    {"nombre": "Marta", "notas": [10, 9]},
    {"nombre": "Carlos", "notas": [2, 3, 1]},
    {"nombre": "Juan", "notas": [6, 4, 8]},
    {"nombre": "Florin", "notas": [10, 3, 8]},
    {"nombre": "Pablo", "notas": [9, 9, 8]},
]
#  Calcular el promedio de un estudiante.
def calcular_promedio(estudiante):
    return sum(estudiante["notas"])/len(estudiante["notas"])
    
# Determinar si un estudiante ha aprobado.
def aprobado(estudiante):
    media = calcular_promedio(estudiante)
    if media >= 5:
        return "Aprobado"
    else:
        return "Suspenso"

# Encontrar al estudiante con la media más alta.
def encontrar_mejor(estudiantes):
    media_mas_alta = 0
    contador = 0
    posicion = 0
    
    for estudiante in estudiantes:
        if calcular_promedio(estudiante) > media_mas_alta:
            media_mas_alta = calcular_promedio(estudiante)
            posicion = contador
            
        contador+=1
        
    return estudiantes[posicion]