## 📝 Ejercicio: Clasificador de contenido de un directorio

### 🎯 Objetivo:
Crear un script en Python que explore un directorio (el actual o uno indicado por el usuario) y **clasifique los elementos** en:
- 📁 **Directorios**
- 📄 **Ficheros ordinarios**

---

### 🛠 Instrucciones:
1. Crea un archivo llamado `clasificar_directorio.py`.
2. El script debe:
   - Limpiar la pantalla al inicio (`subprocess.run(['clear'])`)
   - Aceptar un directorio como argumento (por línea de comandos).
     - Si no se proporciona ninguno, usará el directorio actual.
     - Si el argumento no es un directorio válido, mostrará un mensaje de error.
   - Listar todos los elementos de ese directorio.
   - Mostrar **primero los directorios** y luego los **ficheros**, cada uno con su propio recuento.

---

### 💡 Pistas:
- Usa `os.listdir()` para listar el contenido.
- Usa `os.path.isdir()` y `os.path.isfile()` para clasificarlos.
- Usa `os.path.join()` para construir rutas completas si es necesario.
- Recuerda importar también `sys` y `os`.

---

### 🧪 Ejemplo de salida esperada:

```
📁  Directorios (3):
- pruebas
- datos
- __pycache__

📄  Ficheros (4):
- script.py
- datos.csv
- imagen.png
- terminal_colors.py
```
*El ejemplo es una invención, los nombres de los archivos o de los directorios varian en gran medida de la carpeta en la que queramos que se muestren los datos.*

---

### 🌈 BONUS: Modo con colores ANSI

✔️ Si **importas un módulo externo** llamado `terminal_colors.py` con clases de colores ANSI y los **usas** para resaltar:

- El título de “Directorios” con color azul
- El título de “Ficheros” con color verde
- Los errores en rojo

… obtendrás el **10** 🏅

📌 *Pueden usar la clase `TerminalColors` como se vio en ejercicios anteriores.*


--- 

**Subir un archivo pdf mostrando el resultado obtenido por pantalla del contennedor Docker tras ejecutar el script y el script que habeis programado.**
