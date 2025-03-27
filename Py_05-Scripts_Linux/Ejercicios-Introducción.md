
## 🔰 Nivel 1 – Ejercicios de Introducción

---

### ✅ **Ejercicio 1 – Limpiar la pantalla del terminal**

📌 **Objetivo**: Usar `subprocess.run()` para ejecutar un comando del sistema operativo.

🛠 **Instrucciones**:
1. Crea un script llamado `limpiar_pantalla.py`.
2. Usa `subprocess.run(['clear'])` para borrar la pantalla.
3. Incluye una función llamada `main()` que se ejecute al lanzar el script.
4. Añade un comentario que explique lo que hace cada parte del código.

💡 **Ampliación**: Añadir una espera (`input("Pulsa Enter para continuar...")`) tras limpiar la pantalla.

---

### ✅ **Ejercicio 2 – Mostrar información básica del sistema**

📌 **Objetivo**: Ejecutar comandos básicos del sistema desde Python.

🛠 **Instrucciones**:
1. Crea un script llamado `informacion_sistema.py`.
2. Muestra:
   - El usuario actual (`whoami`)
   - La fecha (`date`)
4. Cada comando debe ejecutarse con `subprocess.run()` desde funciones distintas.
5. Añade separación visual entre los resultados (por ejemplo, líneas con guiones o saltos de línea).

💻 **Salida esperada por consola**:
```
Soy root
Hoy es Martes, 25 de Marzo de 2025 
```

📦 **Sugerencia de estructura**:

```python
def mostrar_usuario():
    pass # Comando whoami

def mostrar_fecha():
    pass # Comando date

def formatear_fecha(fecha:str)
    pass # Función que devuelve la fecha del comando date como cadena de texto formateada correctamente

if __name__ == "__main__":
    pass
```

💡 **Ampliación**: Importar una función `limpiar_pantalla()` al inicio del script.

---

### ✅ **Ejercicio 3 – Crear un menú interactivo**

📌 **Objetivo**: Usar `input()`, bucles y condiciones para interactuar con el usuario.

🛠 **Instrucciones**:
1. Crea un script llamado `menu_sistema.py`.
2. Muestra un menú como el siguiente:
   ```
   1) Mostrar la fecha
   2) Mostrar usuario actual
   3) Añadir un usuario (sin contraseña). Para ello tenemos que ejecutar `adduser #####` al ejecutarlos nos pide una contraseña. Le damos a intro un par de veces.
   4) Mostrar calendario actual
   5) Cambiar contraseña `passwd #####` luego en la terminal establecemos la contraseña que queramos.
   6) Salir
   ```
3. Usa un bucle para pedir al usuario una opción hasta que elija salir.
4. Cada opción debe llamar a una función que ejecute el comando correspondiente.

✔️ **Requisitos**:
- Validar que la entrada del usuario sea un número entre 1 y 6.
- Salir limpiamente con `sys.exit(0)`.

💡 **Ampliación**:
- Añadir colores al menú usando códigos ANSI.
- Añadir más opciones (por ejemplo, mostrar PATH o uso de memoria).

