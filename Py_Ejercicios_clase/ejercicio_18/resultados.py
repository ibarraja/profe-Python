import funciones

estudiantes = funciones.estudiantes

for estudiante in estudiantes:
    
    media = funciones.calcular_promedio(estudiante)
    nombre = estudiante["nombre"]
    estado = funciones.aprobado(estudiante) 
    print(f"{nombre} - {media:.2f} - Estado: {estado}")
    
mejor_estudiante = funciones.encontrar_mejor(estudiantes)
nombre_mejor_estudiante = mejor_estudiante["nombre"]
media_mejor_estudiante = funciones.calcular_promedio(mejor_estudiante)
print(f"El mejor estudiante es: {nombre_mejor_estudiante} con un {media_mejor_estudiante:.2f}")
