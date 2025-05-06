## 📘 Ejercicio `e6.py` – Simulador de creación de usuarios en Alpine Docker

### 🎯 Objetivo:

Crear un script en Python que **añada usuarios simulados** editando directamente el archivo `/etc/passwd` dentro de un contenedor Docker basado en Alpine Linux.

---

### 🛠 Instrucciones:

1. El script debe llamarse `e6.py`.
2. Debe ejecutarse pasando como argumentos los nombres de usuario que se quieren crear:

```bash
python3 e6.py javi maria pedro
```

3. Cada usuario se añadirá al archivo `/etc/passwd` simulando su creación, con una línea como:

```
usuario:x:UID:GID::/home/usuario:/bin/sh
```

4. El UID y el GID se calcularán a partir del **UID más alto ya existente** en el archivo `/etc/passwd`.
5. Si **ya existe un usuario con ese nombre**, se mostrará un mensaje de error.
6. Si **no se pasa ningún argumento**, el script debe mostrar un mensaje de error y finalizar correctamente.

---

### ✅ Requisitos técnicos:

* Usar variables globales para los mensajes de error:

```py
ERROR_SIN_ARGUMENTOS = "⚠️ Debes indicar al menos un nombre de usuario."
ERROR_USUARIO_EXISTE = "❌ El usuario '{usuario}' ya existe."
```

* Implementar manejo de errores con `try` y `except` (no usar `raise` directamente).
* Comprobar si el usuario ya existe antes de intentar añadirlo.
* Simular la escritura con:

```py
subprocess.run(f"echo '{linea}' >> /etc/passwd", shell=True)
```

---

### 💡 Sugerencias:

* Implementa una función `obtener_uid_maximo()` que recorra `/etc/passwd` y devuelva el UID más alto.
* Evita que usuarios como `nobody` o `root` interfieran en los resultados.

---

### 📦 Salida esperada:

```
✅ Usuario simulado 'javi' añadido con UID 1001
✅ Usuario simulado 'maria' añadido con UID 1002
❌ El usuario 'pedro' ya existe.
```

---

## 📘 Ejercicio `e7.py` – Mostrar usuarios simulados del sistema

### 🎯 Objetivo:

Crear un script que lea el archivo `/etc/passwd` y **muestre solo los usuarios simulados** creados con `e6.py`.

---

### 🛠 Instrucciones:

1. El script debe llamarse `e7.py`.
2. Debe leer `/etc/passwd` y mostrar en pantalla:

   * El nombre de usuario.
   * Su UID.
3. Solo se mostrarán usuarios con:

   * UID ≥ 1000
   * Distintos de `nobody`
3. Modificar `/etc/passwd` para que todos los usuarios con uid >= 1001 y < 2000 que empiecen por la misma letra los agrupen en el mismo GID: 1001
---

### 📦 Salida esperada:

```
Usuarios simulados (3):
- javi (UID 1001)
- maria (UID 1002)
- alumno1 (UID 1003)
```

---

### 💡 Sugerencia:

* Usa `split(":")` para procesar las líneas.
* Utiliza control de errores mínimo (evitar excepciones si el archivo no existe o una línea está mal formada).

