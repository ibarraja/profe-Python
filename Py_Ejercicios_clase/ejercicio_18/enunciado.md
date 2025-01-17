### Ejercicio 18: Gestión de notas de estudiantes

Crea un programa dividido en dos archivos que realice las siguientes tareas:

1. Reciba una lista de estudiantes con sus nombres y sus notas.
2. Calcule la media de cada estudiante.
3. Determine si cada estudiante ha aprobado (promedio >= 5.0) o no.
4. Identifique al estudiante con la media más alta y muestre su nombre junto con el promedio.

#### **Requisitos del programa:**

1. **Archivo `funciones.py`:**
   - Define la lista de estudiantes:
   ```python
   estudiantes = [
       {"nombre": "Ana", "notas": [7, 8, 6]},
       {"nombre": "Luis", "notas": [4, 5, 3]},
       {"nombre": "Marta", "notas": [10, 9]},
       {"nombre": "Carlos", "notas": [2, 3, 1]},
       {"nombre": "Juan", "notas": [6, 4, 8]},
       {"nombre": "Florin", "notas": [10, 3, 8]},
       {"nombre": "Pablo", "notas": [9, 9, 8]},
       ...
   ]
   ```
   - Implementa las funciones necesarias para:
     - Calcular el promedio de un estudiante.
     - Determinar si un estudiante ha aprobado.
     - Encontrar al estudiante con la media más alta.

2. **Archivo `resultados.py`:**
   - Importa las funciones y la lista desde `funciones.py`.
   - Usa las funciones para procesar la lista de estudiantes.
   - Muestra los resultados por consola de forma clara:
     - Nombre del estudiante.
     - Su promedio.
     - Si ha aprobado o no.
     - El estudiante con la media más alta.

#### **Ejemplo de salida esperada:**
```
Ana - Promedio: 7.00 - Estado: Aprobado
Luis - Promedio: 4.00 - Estado: Reprobado
Marta - Promedio: 9.50 - Estado: Aprobado
Carlos - Promedio: 2.00 - Estado: Reprobado
El mejor estudiante es Marta con un promedio de 9.50
```

**Nota:** Asegúrate de estructurar el código correctamente para separar la lógica del procesamiento de los datos y la presentación de resultados.
