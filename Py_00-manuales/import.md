# `import` en Python
El comando `import` en Python permite acceder a módulos y bibliotecas externas o internas, ampliando las funcionalidades del lenguaje sin necesidad de escribir código desde cero. Los módulos son archivos que contienen definiciones y declaraciones de funciones, clases y variables de funciones que pueden ser utilzadas en otros programas.

## 1. ¿Qué es un módulo?
Un módulo es un archivo de Python que contiene definiciones  (como funciones y clases) y código que se puede reutilziar en otros programas. Python incluye una biblioteca estándar que contiene, módulos útiles, pero también puedes instalar bibliotecas externas.

### Sintaxis básica para importar módulos
1. **Importar un módulo completo:**
```python
import nombre_modulo
```
2. **Importar un elemento específico de un módulo:**
```python
from nombre_modulo import nombre_elemento
```
3. **Importar con un alias (nombre corto):**
```python
import nombre_modulo as alias
```
4. **Importar todos los elementos de un módulo (no recomendado):**
```python
from nombre_modulo import *
```
## 2. Importar Módulos
En Python, los módulos que contienen código reutilizable pueden ser importados en otros programas. Los módulos pueden ser **locales** (creados por el usuario o incluidos en el proyecto), **estándar** que forman parte de la biblioteca estándar de Python, como `math` y `datetime` ( no requieren instalación previa) y **externos** (necesitan instalación previa con herramientas como `pip`).

### 2.1 Importar Módulos Locales
Los módulos locales son archivos `.py` que están en el mismo directorio del programa principal o en una ubicación accesible dentro del entorno Python.

#### ¿Cómo importar un módulo local?
1. **Crear un archivo Python con funciones o clases reutilizables** (módulo local).
2. **Asegurarse de qye el archivo está en el mismo directorio o en una ruta accesible.**
3. Usa la instrucción `import` para usar el módulo

#### Ejemplo
**Estructura de archivos:**
```makefile
Copiar código
mi_proyecto/
│
├── principal.py
├── utilidades.py
```
**Contenido de** `utilidades.py`:
```python
def saludar(nombre):
    return f"Hola, {nombre}! Bienvenido a Python."
```

**Contenido de** `principal.py`:

```python
import utilidades  # Importar el módulo local

# Usar una función del módulo
mensaje = utilidades.saludar("Juan")
print(mensaje)
```
**Salida:**
```makefile
Hola, Juan! Bienvenido a Python.
```
#### Importar elementos específicos de un módulo local
Puedes importar funciones, clases o variables específicas de un módulo local:

```python
from utilidades import saludar

mensaje = saludar("Ana")
print(mensaje)
```

#### Configurar rutas para importar módulos
Si el módulo no está en el mismo directorio, debes añadir su ruta al entorno de Python. Puedes hacerlo con el módulo `sys`:

```python
import sys
sys.path.append("ruta/a/tu/modulo")  # Añade la ruta donde está el módulo

import utilidades
```

### 2.2 Importar Módulos Estándar
Un módulo estándar es parte de la biblioteca estándar de Python. Estos módulos vienen incluidos con cualquier instalación oficial de Python y no necesitan ser instalados por separado con pip. Contienen funcionalidades predefinidas para realizar tareas comunes, como manipular fechas, realizar operaciones matemáticas, manejar archivos, etc.

Para importar los modulos simplemente tendremos que escribir los siguiente:
```python
import math
import datetime
import json
```

#### Principales módulos Estándar de Python:
##### 1. Manipulación de datos básicos:
- `math`: Funciones matemáticas avanzadas (trigonometría, logaritmos, potencias).
- `random`: Generación de números aleatorios.
- `statistics`: Cálculos estadísticos básicos como media, mediana y desviación estándar.
- `decimal`: Manejo de números decimales con mayor precisión.
- `fractions`: Manejo de números racionales como fracciones.

##### 2. Fechas y horas
- `datetime`: Manejo de fechas y horas.
- `time`: Funciones relacionadas con la medición del tiempo.
- `calendar`: Generación y manipulación de calendarios.
- `zoneinfo`: Manejo de zonas horarias.
##### 3. Manejo de archivos y directorios
- `os`: Interacción con el sistema operativo.
- `sys`: Para manejar la entrada y salida estándar, trabajar con argumentos de línea de comandos, y más.
- `shutil`: Operaciones con archivos y directorios, como copiar o mover.
- `pathlib`: Manejo avanzado de rutas de archivos.
- `glob`: Búsqueda de archivos y directorios usando patrones.
- `tempfile`: Creación de archivos y directorios temporales.
##### 4. Procesamiento de texto
- `re`: Expresiones regulares para buscar y manipular texto.
- `textwrap`: Ajuste y formateo de texto.
- `unicodedata`: Manipulación de datos Unicode.
- `string`: Constantes y funciones para manipulación de cadenas.
##### 5. Entrada/Salida (I/O)
- `io`: Manejo de flujos de entrada y salida.
- `csv`: Lectura y escritura de archivos CSV.
- `json`: Codificación y decodificación de datos en formato JSON.
- `pickle`: Serialización y deserialización de objetos Python.
- `xml.etree.ElementTree`: Análisis y generación de datos en formato XML.
##### 6. Cálculos numéricos y científicos
- `array`: Manejo de matrices de datos básicos.
- `cmath`: Funciones matemáticas para números complejos.
- `itertools`: Iteradores para manipulación eficiente de datos.
- `functools`: Herramientas para manipular funciones y decoradores.
##### 7. Redes e Internet
- `socket`: Comunicación a través de redes (TCP/IP, UDP).
- `http`.client: Realización de solicitudes HTTP.
- `urllib`: Trabajar con URLs (descargar datos, analizar URLs, etc.).
- `email`: Manejo de correos electrónicos.
- `ssl`: Soporte para conexiones seguras (SSL/TLS).
##### 8. Desarrollo web
- `cgi`: Interacción con aplicaciones CGI.
- `html`: Manipulación de datos en formato HTML.
- `http`.server: Configuración de servidores HTTP básicos.
- `xml`: Análisis y generación de datos XML.
##### 9. Pruebas y depuración
- `unittest`: Marco para pruebas unitarias.
- `logging`: Registro de mensajes de depuración e información.
- `traceback`: Manejo de trazas de errores.
- `pdb`: Depurador interactivo para Python.
##### 10. Interacción con el sistema operativo
- `sys`: Acceso a variables y funciones relacionadas con el intérprete de Python.
- `os`: Interacción con el sistema operativo (archivos, procesos, etc.).
- `subprocess`: Ejecución de comandos externos y scripts.
- `platform`: Información sobre la plataforma en la que se ejecuta Python.
##### 11. Programación concurrente
- `threading`: Programación multihilo.
- `multiprocessing`: Paralelismo utilizando múltiples procesos.
- `asyncio`: Programación asíncrona.
- `queue`: Colas seguras para intercambio de datos entre hilos.
##### 12. Seguridad y criptografía
- `hashlib`: Algoritmos de hash como SHA256 o MD5.
- `hmac`: Algoritmos de autenticación basados en claves.
- `secrets`: Generación de contraseñas y claves criptográficas seguras.
##### 13. Utilidades generales
- `argparse`: Análisis de argumentos de línea de comandos.
- `configparser`: Manejo de archivos de configuración.
- `dataclasses`: Manejo de clases ligeras para datos.
- `collections`: Estructuras de datos especializadas (colas, contadores, etc.).
- `typing`: Soporte para anotaciones de tipos.
- `uuid`: Generación de identificadores únicos universales (UUID).
##### 14. Gráficos y visualización
- `tkinter`: Desarrollo de interfaces gráficas (GUIs).
#### ¿Cómo saber qué módulos están disponibles?
Puedes obtener una lista de todos los módulos estándar disponibles en tu versión de Python ejecutando el siguiente comando de Python:

```python
help("modules")
```

### 2.3 Importar Módulos Externos
Los módulos externos son bibliotecas desarrolladas por terceros, disponibles en el repositorio oficial de Python (PyPI) y que requieren instalación previa con `pip`. Para importar los modulos simplemente tendremos que escribir los siguiente:

Por ejemplo, para instalar el módulo `requests`:
```bash
pip install requests
```
El módulo `requests` facilita el trabajo con solicitudes HTTP en Python.

**Código:**

```python
import requests

respuesta = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(respuesta.json())  # Convertir la respuesta a JSON
```

**Salida:**

```json
{
    "userId": 1,
    "id": 1,
    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
    "body": "quia et suscipit..."
}
```
#### ¿Qué es pip?
`pip` es el administrador de paquetes de Python que permite instalar, actualizar y desinstalar módulos o bibliotecas externas.

**Instalar un módulo con `pip`**
Usa el comando `pip install` seguido del nombre del módulo para instalarlo.

```bash
pip install nombre_modulo
```

#### Instalar y Usar un Módulo con Dependencias
Algunos módulos externos requieren otros módulos para funcionar. pip se encarga de instalar automáticamente las dependencias necesarias.

Instalar un módulo con una versión específica
Puedes especificar la versión exacta o un rango compatible:

```bash
pip install requests==2.26.0  # Versión específica
pip install requests>=2.20.0  # Versión igual o superior a 2.20.0
```
#### Listar módulos instalados
```bash
pip list
```
#### Desinstalar un módulo
```bash
pip uninstall nombre_modulo
```