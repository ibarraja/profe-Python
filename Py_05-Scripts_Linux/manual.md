# 📘 Manual de Python: Uso de `subprocess` y `sys.argv` para crear scripts en Linux

---

## 💻 Antes de comenzar: Configura tu entorno con Docker (opcional pero recomendable)

Si quieres trabajar en un entorno limpio y controlado sin afectar tu sistema operativo, puedes usar Docker. A continuación te explico cómo montar uno:

1. **Crea una carpeta en tu Escritorio** llamada, por ejemplo, `python-docker`.
2. Dentro de esa carpeta, crea un archivo llamado `Dockerfile` con el siguiente contenido:

```Dockerfile
FROM python:3.10.2-alpine3.15
RUN mkdir /python
WORKDIR /python
CMD ["tail", "-f", "/dev/null"]
```

3. Abre una terminal en esa carpeta y ejecuta este comando para construir la imagen:

```bash
docker build -t python-pruebas:0.1 .
```

Esto creará una imagen ligera de Python basada en Alpine Linux, con una carpeta `/python` lista para trabajar. Puedes usar esta imagen como entorno de pruebas ejecutando:

Una vez tengamos la imagen creada, tendremos que montar el contenedor. Abrimos Docker Desktop y nos dirigimos a images. Ejecutamos la imagen recien creada y **muy** importante, tendremos que darle a Optinal Settings, donde tendremos que añadir un nombree descriptivo al Contendor y linkear la carpeta creada en el escritorio con la  de `/python`.

👀¡Cuidado! Ten en cuenta que el sistema de naavegacion de windows son contrabarras: `\` y en Linux es la barra: `/`.

---

## 🌟 Introducción

Una de las grandes ventajas de Python es su capacidad para integrarse con el sistema operativo. En entornos **Linux**, es habitual automatizar tareas mediante **scripts**: pequeños programas que ejecutan comandos del sistema, analizan argumentos y generan salidas útiles. Para ello, los módulos más comunes son:

- `subprocess`: permite ejecutar comandos del sistema como si estuviésemos en la terminal.
- `sys.argv`: permite capturar los argumentos que recibe un script cuando se lanza desde la línea de comandos.

Este manual te guiará paso a paso en su uso, combinando teoría, ejemplos y buenas prácticas.

---

## 🧰 Módulo `subprocess`: Ejecutar comandos del sistema

### 🤔 ¿Qué es `subprocess`?

Es un módulo de la biblioteca estándar de Python que permite **lanzar procesos del sistema operativo** (como `ls`, `ping`, `cal`, etc.). Es una alternativa moderna y segura a funciones antiguas como `os.system()`.

---

### ⚖️ `subprocess.run()`: la forma estándar de ejecutar comandos

```python
import subprocess
subprocess.run(["ls", "-l"])
```

Este comando ejecuta `ls -l` como si lo hiciéramos desde una terminal.

#### 🔍 ¿Qué devuelve?

`run()` devuelve un objeto `CompletedProcess`, con:
- `args`: argumentos del comando.
- `stdout`: salida estándar (si se captura).
- `stderr`: errores (si se captura).
- `returncode`: código de salida (0 = éxito).

---

### ✅ Captura de salida:

```python
resultado = subprocess.run(["date"], capture_output=True, text=True)
print("Hoy es:", resultado.stdout)
```

---

### ⚠️ Control de errores:

```python
resultado = subprocess.run(["ls", "/no_existe"], capture_output=True, text=True)
if resultado.returncode != 0:
    print("Error:", resultado.stderr)
```

---

### 💡 Buenas prácticas:
- Usa listas (`["ls", "-l"]`) en lugar de cadenas.
- Evita `shell=True` si no es necesario.
- Controla errores con `returncode` o `check=True`.

---

## 🧪 `subprocess.getoutput()`: forma rápida y directa

### 🤔 ¿Qué es?

Ejecuta un comando y devuelve su salida como texto. Internamente usa `shell=True`.

```python
from subprocess import getoutput
usuario = getoutput("whoami")
print("Usuario actual:", usuario)
```

### 🔍 Cuándo usarlo:

| Ideal para...                 | No recomendado si...               |
|------------------------------|------------------------------------|
| Comandos simples             | Se necesitan errores (`stderr`)    |
| Sin entradas del usuario     | Hay riesgo de inyección           |

---

### 📅 Ejemplo:

```python
print(getoutput("date"))
```

---

## 🚫 Peligro real: inyección de comandos con `shell=True`

Usar `shell=True` **con entradas del usuario** puede ser peligroso:

```python
import subprocess
nombre = input("Tu nombre: ")
subprocess.run(f"echo Hola {nombre}", shell=True)
```

Si el usuario escribe:
```
Javier && rm -rf ~
```
Se ejecutaría:
```bash
echo Hola Javier && rm -rf ~
```
🚨 Podría eliminar el directorio personal.

### ✅ ¿Cómo evitarlo?
1. **Evita `shell=True`** si no es imprescindible.
2. **Nunca uses inputs sin filtrar** directamente en comandos.
3. Usa `shlex.quote()` para proteger entradas si no hay alternativa.

---

## 💬 Módulo `sys.argv`: Argumentos desde la terminal

### 🤔 ¿Qué es?

Permite recibir datos desde la terminal al ejecutar scripts:

```bash
python3 saludo.py Javier
```

```python
import sys
print("Hola,", sys.argv[1])
```

### 🔢 Lista `sys.argv`:
- `sys.argv[0]`: nombre del script.
- `sys.argv[1:]`: argumentos reales.

### 🔹 Recorriendo argumentos:

```python
for i, arg in enumerate(sys.argv[1:], start=1):
    print(f"Argumento {i}: {arg}")
```

### ⚠️ Validación de argumentos:

```python
if len(sys.argv) != 3:
    print("Uso: script.py <mes> <año>")
    sys.exit(1)
```

## 🔗 Ejemplo combinado: argumentos + comandos

```python
import sys
import subprocess

if len(sys.argv) != 3:
    print("Uso: script.py <mes> <año>")
    sys.exit(1)

mes, anio = sys.argv[1], sys.argv[2]
subprocess.run(["cal", mes, anio])
```

---
 
## 📂 Módulo `os`: Acceso al sistema de archivos

### 📁 `os.listdir()` – Listar contenido de un directorio

Devuelve una lista con los nombres de todos los elementos del directorio indicado:

```python
import os
print(os.listdir("/home"))  # Muestra los ficheros de /home
```

Si no se indica una ruta, devuelve los elementos del directorio actual:

```python
os.listdir()  # Equivale a os.listdir(os.getcwd())
```

### ✅ Comprobar si es fichero o directorio

```python
os.path.isdir("ruta")    # True si es un directorio
os.path.isfile("ruta")   # True si es un fichero ordinario
```

### 📌 Obtener el directorio actual

```python
os.getcwd()  # Devuelve la ruta completa del directorio desde el que se ejecuta el script
```

### 🧪 Combinando rutas

Cuando trabajamos con rutas relativas, es buena práctica usar:

```python
os.path.join(directorio, nombre_archivo)
```

---

## 🔗 Ejemplo: Clasificación de ficheros y directorios

```python
import os
ruta = "/etc"
for elemento in os.listdir(ruta):
    ruta_completa = os.path.join(ruta, elemento)
    if os.path.isdir(ruta_completa):
        print(f"📁   {elemento}")
    elif os.path.isfile(ruta_completa):
        print(f"📄   {elemento}")
```

---

Con estos elementos puedes desarrollar scripts que naveguen por directorios, muestren contenido clasificado y acepten rutas como argumentos. La práctica con `os` es esencial para la administración de sistemas, automatización y creación de herramientas personalizadas.
