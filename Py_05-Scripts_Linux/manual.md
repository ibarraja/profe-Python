# 📘 Manual de Python: Uso de `subprocess` y `sys.argv` para crear scripts en Linux

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

---

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

