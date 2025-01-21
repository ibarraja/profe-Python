# Crea un programa que reciba una lista de estudiantes con sus nombres y sus notas, calcule el promedio de cada estudiante, determine quién aprobó (promedio >= 5.0) y quién no, y devuelva el estudiante con la nota promedio más alta. Hay errores intencionales para depuración.

# Función para calcular el promedio de un estudiante
def calcular_promedio(notas):
    total = sum(notas)
    promedio = total / len(notas)
    return promedio

# Función para encontrar al estudiante con el promedio más alto
def mejor_estudiante(estudiantes):
    mejor = ""
    mayor_promedio = -1
    for estudiante in estudiantes:
        promedio = calcular_promedio(estudiantes["notas"])
        if promedio > mayor_promedio:
            mayor_promedio = promedio
            mejor = estudiantes["nombre"]
    return mejor, mayor_promedio

# Lista de estudiantes con errores intencionales
estudiantes = [
    {"nombre": "Ana", "notas": [7, 8, 6]},
    {"nombre": "Luis", "notas": [4, 5, 3]},
    {"nombre": "Marta", "notas": [10, 9]},  # Nota promedio más alta
    {"nombre": "Carlos", "notas": [2, 3, 1]},
]

# Calcular promedios y determinar aprobados
for estudiante in estudiantes:
    promedio = calcular_promedio(estudiantes["notas"])  # Error: debería ser estudiante["notas"]
    if promedio >= 5:
        estado = "Aprobado"
    else:
        estado = "Suspenso"
    print(f"{estudiante['nombre']} - Promedio: {promedio:.2f} - Estado: {estado}")

# Encuentra el mejor estudiante
mejor, promedio = mejor_estudiante(estudiantes)
print(f"El mejor estudiante es {mejor} con un promedio de {promedio:.2f}")
