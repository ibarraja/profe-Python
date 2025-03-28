### 🔁 **Ejercicio 4 – Versión mejorada: Analizador de argumentos**

📌 **Objetivo**: Detectar el tipo de cada argumento y analizar su contenido.

🛠 **Nueva propuesta**:
- Crear un script `analizar_argumentos.py`.
- Por cada argumento recibido:
  - Indicar si es un número entero, decimal, palabra o combinación.
  - Mostrar su longitud.
  - Si es numérico, decir si es par/impar (si entero), o positivo/negativo.
- Mostrar cuántos argumentos de cada tipo se han recibido.

📦 **Ejemplo de salida**:
```
Argumento 1: 42 → Entero (par)
Argumento 2: hola → Texto (longitud 4)
Argumento 3: -3.5 → Decimal negativo
Argumento 4: prueba123 → Mixto

Resumen:
Enteros: 1
Decimales: 1
Textos: 1
Mixtos: 1
```

💡 **Ampliación**:
- Usar funciones para clasificar los argumentos.
- Añadir colores según tipo de dato.

---

### 📆 **Ejercicio 5 – Versión mejorada: Calendario inteligente**

📌 **Objetivo**: Permitir múltiples formas de entrada y añadir funcionalidades extra al uso de `cal`.

🛠 **Propuesta**:
- Script `calendario_inteligente.py` que acepte:
  - Solo el año → muestra todo el año (`cal -y`)
  - Solo el mes → asume el año actual
  - Mes y año (en cualquier orden)
  - También admite el mes como texto
- Añadir opción `--festivos` (opcional) que imprima si el mes contiene algún festivo nacional (definido en un diccionario).

📦 **Ejemplo de uso**:
```bash
$ python3 calendario_inteligente.py 3 2024
$ python3 calendario_inteligente.py abril
$ python3 calendario_inteligente.py --festivos 12 2025
```

**Array Festivos:** Podéis usar este diccionario para poder localizar los festivos.
```py
festivos = {
    1: [(1, "Año Nuevo"), (6, "Día de Reyes")],
    3: [(29, "Viernes Santo")],  # Variable: puedes calcularlo si quieres más precisión
    5: [(1, "Día del Trabajo")],
    8: [(15, "Asunción de la Virgen")],
    10: [(12, "Fiesta Nacional de España")],
    11: [(1, "Día de Todos los Santos")],
    12: [
        (6, "Día de la Constitución Española"),
        (8, "Inmaculada Concepción"),
        (25, "Navidad")
    ]
}
```

📦 **Salida adicional (modo festivos)**:
```
Diciembre contiene los siguientes festivos en España:
- 6: Día de la Constitución
- 8: Inmaculada Concepción
- 25: Navidad
```

💡 **Sugerencias técnicas**:
- Usar `datetime` para obtener el año actual.
- Crear un diccionario `festivos = {12: [(6, 'Constitución'), (8, 'Inmaculada'), (25, 'Navidad')], ...}`.
- Validar argumentos flexibles con `argparse` o estructura propia.

---
