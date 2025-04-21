# ✅ Ejercicio 1: Calendario del mes actual

# Este script muestra el calendario del mes actual utilizando el comando `cal`
# y el módulo datetime para obtener el mes y el año actual.

import subprocess
from datetime import datetime

# Paso 1: Obtener la fecha de hoy
today = datetime.now()
mes = today.month
anio = today.year

# Paso 2: Mostrar por pantalla el mes y el año
print(f"\n📅 Calendario del mes {mes} del año {anio}\n")

# Paso 3: Ejecutar el comando `cal` con subprocess
subprocess.run(["cal", str(mes), str(anio)])


# ✅ Ejercicio 2: Listar archivos del directorio actual

# Este script utiliza `os.listdir()` para mostrar los archivos y carpetas
# que hay en el directorio actual.

import os

# Paso 1: Obtener el listado de archivos
elementos = os.listdir()

# Paso 2: Mostrar cada elemento numerado
print("\n📁 Contenido del directorio actual:\n")
for i, nombre in enumerate(elementos, start=1):
    print(f"{i}) {nombre}")
