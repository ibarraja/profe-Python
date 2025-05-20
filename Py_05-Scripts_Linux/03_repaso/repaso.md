# Ejercicio: Búsqueda interactiva de texto en archivos con `grep` y gestión avanzada de errores

---

## Objetivo

Crear un script en Python que permita buscar recursivamente un término dentro de un directorio usando el comando `grep -r`. El script debe poder recibir los datos por argumentos o solicitarlos interactivamente, gestionar la ejecución y errores, y ofrecer un menú para repetir búsquedas o cambiar directorio antes de salir.

---

## Enunciado detallado

Desarrolla un script llamado `buscar_texto.py` que cumpla lo siguiente:

### 1. Modo de entrada de datos: argumentos o interactivo

* El script puede recibir dos argumentos por línea de comandos:

  * El término a buscar (cadena).
  * El directorio donde buscar.

* Si **faltan uno o ambos argumentos**, el script debe entrar en modo interactivo donde:

  * Pide al usuario que introduzca el término a buscar (por teclado).
  * Pide al usuario que introduzca el directorio donde buscar.

### 2. Ejecución de la búsqueda

* Ejecutar `grep -r <termino> <directorio>` usando `subprocess.run()` con `capture_output=True` y `text=True`.
* Procesar la salida según el código de retorno (`returncode`):

  | Código de retorno                                                     | Significado                                       | Acción del script                                                               |
  | --------------------------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------------------------------------- |
  | 0                                                                     | Coincidencias encontradas                         | Mostrar archivos únicos donde aparece el término y número total de ocurrencias. |
  | 1                                                                     | No se encontraron coincidencias                   | Mostrar mensaje:                                                                |
  | `"No se encontraron coincidencias para '<termino>' en <directorio>."` |                                                   |                                                                                 |
  | 2                                                                     | Error en ejecución (p. ej., directorio no existe) | Mostrar mensaje de error con detalle técnico y pedir acción.                    |

### 3. Menú interactivo tras cada búsqueda

Después de mostrar el resultado, el script debe ofrecer un menú con opciones:

* **1) Nueva búsqueda con mismo directorio**
* **2) Cambiar directorio**
* **3) Salir del programa**

Según la opción seleccionada:

* Si elige nueva búsqueda, pide un nuevo término y repite la búsqueda.
* Si elige cambiar directorio, pide la nueva ruta y luego pide término para buscar.
* Si elige salir, finaliza el programa.

### 4. Validaciones

* Validar que el directorio existe y es accesible.
* Validar que el término no esté vacío.
* Controlar entradas incorrectas y ofrecer mensajes claros para que el usuario pueda corregir.

### 5. Uso desde línea de comandos

* Si se proporcionan ambos argumentos, el script realiza la búsqueda una sola vez y termina.
* Si se proporcionan menos de dos argumentos, entra en modo interactivo con el menú descrito.

---

## Ejemplo de ejecución interactiva

```plaintext
$ python3 buscar_texto.py

Introduce el término a buscar: error
Introduce el directorio donde buscar: /var/log

El término 'error' se encontró en 3 archivos:
 - /var/log/syslog
 - /var/log/auth.log
 - /var/log/dmesg
Número total de ocurrencias encontradas: 17

¿Qué deseas hacer?
1) Nueva búsqueda con mismo directorio
2) Cambiar directorio
3) Salir
Selecciona una opción: 1

Introduce el término a buscar: fallo

No se encontraron coincidencias para 'fallo' en /var/log.

¿Qué deseas hacer?
1) Nueva búsqueda con mismo directorio
2) Cambiar directorio
3) Salir
Selecciona una opción: 3

Saliendo del programa...
```

---

## Notas

* El script debe manejar correctamente todos los posibles errores de `grep` y las entradas del usuario.
* La experiencia de usuario debe ser clara, con mensajes comprensibles y menús fáciles de usar.
* Se recomienda modularizar el código en funciones para mejorar su mantenimiento.

