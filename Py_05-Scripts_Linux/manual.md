¡Entendido, Javier! A continuación, te presento una **versión ampliada del manual**, con una redacción más pedagógica, explicaciones conceptuales antes del código, y contexto sobre para qué sirve cada herramienta, cómo se usa en entornos reales de scripting en Linux, y cuándo elegir una u otra. También añadiré observaciones de buenas prácticas y ejemplos más conectados a situaciones reales.

---

# 📘 Manual de Python: Uso de `subprocess` y `sys.argv` para crear scripts en Linux

---

## 🎯 Introducción

Una de las grandes ventajas de Python es su capacidad para integrarse con el sistema operativo. En entornos **Linux**, es habitual automatizar tareas mediante **scripts**: pequeños programas que ejecutan comandos del sistema, analizan argumentos y generan salidas útiles. Para ello, los módulos más comunes son:

- `subprocess`: permite ejecutar comandos del sistema como si estuviésemos en la terminal.
- `sys.argv`: permite capturar los argumentos que recibe un script cuando se lanza desde la línea de comandos.

Este manual te guiará paso a paso en su uso, combinando teoría, ejemplos y buenas prácticas.

---

## 🧰 Módulo `subprocess`: Ejecutar comandos del sistema

---

### 🧠 ¿Qué es `subprocess`?

Es un módulo de la biblioteca estándar de Python que permite **lanzar procesos del sistema operativo** (como `ls`, `ping`, `cal`, etc.). Es una alternativa moderna y segura a funciones antiguas como `os.system()`.

---

### 🔧 `subprocess.run()`: la forma estándar de ejecutar comandos

```python
import subprocess

subprocess.run(["ls", "-l"])
```

🔍 Este comando ejecuta `ls -l` como si lo hiciéramos desde una terminal.

#### 🔹 ¿Qué devuelve?

`run()` devuelve un objeto de tipo `CompletedProcess`, con atributos como:

- `args`: los argumentos del comando ejecutado.
- `stdout`: la salida estándar (solo si se ha capturado).
- `stderr`: los errores (si se han capturado).
- `returncode`: código de salida (0 si todo fue bien, diferente si hubo error).

---

### ✅ Ejemplo completo con captura de salida:

```python
resultado = subprocess.run(["date"], capture_output=True, text=True)
print("Hoy es:", resultado.stdout)
```

📌 Aquí usamos dos parámetros:
- `capture_output=True`: indica que queremos capturar la salida (en vez de verla en pantalla).
- `text=True`: convierte la salida de **bytes** a **texto legible**.

---

### ⚠️ Control de errores: verificar si el comando falló

```python
resultado = subprocess.run(["ls", "/carpeta_inexistente"], capture_output=True, text=True)

if resultado.returncode != 0:
    print("Error:", resultado.stderr)
```

✅ Esta verificación es útil en scripts que gestionan archivos, redes, usuarios, etc., para saber si un comando ha funcionado antes de continuar.

---

### 💡 Buenas prácticas al usar `subprocess.run()`:

- Siempre usa listas: `["ls", "-l"]` en vez de un solo string `"ls -l"`.
- Evita `shell=True` salvo que sea imprescindible.
- Valida y controla errores con `returncode` o `check=True`.

---

## 🧪 `subprocess.getoutput()`: forma rápida y directa

### 🧠 ¿Qué es?

Una alternativa más simple que **ejecuta un comando** y **devuelve su salida como cadena de texto**. Internamente usa `os.popen()` y ejecuta con `shell=True`.

```python
from subprocess import getoutput

usuario = getoutput("whoami")
print("Estás logueado como:", usuario)
```

---

### 🔍 Cuándo usar `getoutput()`:

| Ideal para...                     | No recomendado si...                      |
|----------------------------------|-------------------------------------------|
| Tareas simples de lectura        | Hay que capturar errores (`stderr`)       |
| Comandos conocidos y seguros     | Se usan entradas del usuario              |
| Salida inmediata sin estructura  | Se necesita separar stdout/stderr         |

🔐 *OJO:* `getoutput()` ejecuta con `shell=True`, lo que puede ser **inseguro si se usan entradas sin validar**.

---

### 🧪 Ejemplo útil:

```python
fecha = getoutput("date")
directorio = getoutput("pwd")
print(f"Hoy es {fecha}, estás en: {directorio}")
```

---

## 💬 Módulo `sys.argv`: Argumentos desde la terminal

---

### 🧠 ¿Qué es?

Cuando ejecutamos un script con:

```bash
python3 mi_script.py hola mundo
```

Podemos acceder a `"hola"` y `"mundo"` desde el código usando `sys.argv`.

---

### 🧱 Sintaxis básica:

```python
import sys

print("Nombre del script:", sys.argv[0])
print("Argumentos:", sys.argv[1:])
```

🧠 `sys.argv` es una lista:
- `sys.argv[0]`: nombre del archivo (`mi_script.py`)
- `sys.argv[1:]`: argumentos reales

---

### 🧩 Ejemplo práctico:

```python
import sys

if len(sys.argv) < 2:
    print("Por favor, introduce tu nombre")
else:
    print(f"¡Hola, {sys.argv[1]}!")
```

---

### 🔢 Recorriendo argumentos uno a uno:

```python
for i, arg in enumerate(sys.argv[1:], start=1):
    print(f"Argumento {i}: {arg}")
```

Esto permite identificar cada argumento de forma ordenada.

---

### ❗ Validar número y tipo de argumentos:

```python
if len(sys.argv) != 3:
    print("Uso: python3 script.py <mes> <año>")
    sys.exit(1)
```

También puedes validar si el argumento es numérico usando `isdigit()` o `try: int(...)`.

---

## 🔗 Ejemplo conjunto: `subprocess + sys.argv`

```python
import subprocess
import sys

if len(sys.argv) != 3:
    print("Uso: python3 calendario.py <mes> <año>")
    sys.exit(1)

mes = sys.argv[1]
año = sys.argv[2]

# Ejecutar cal
subprocess.run(["cal", mes, año])
```

---

## 🧠 Conclusión y consejos finales

- `subprocess.run()` es la herramienta principal para ejecutar comandos de forma segura y controlada.
- `getoutput()` es útil para tareas simples y rápidas, pero requiere precaución.
- `sys.argv` permite adaptar tus scripts a distintos contextos de uso real (como argumentos de fecha, ruta, nombre de usuario...).
- Validar argumentos y controlar errores es fundamental en scripting real para evitar fallos o comportamientos peligrosos.

---

¿Te gustaría que convierta esto en un documento PDF con portada, tabla de contenidos, ejercicios y actividades al final para reforzar lo aprendido?
