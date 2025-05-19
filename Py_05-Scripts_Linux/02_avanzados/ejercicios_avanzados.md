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
3. Modificar `/etc/passwd` para que todos los usuarios con `UID >= 1001 y < 2000` que empiecen por la misma letra los agrupen en el mismo GID
---

### 📦 Salida esperada:

```
Usuarios simulados (3):
- javi (UID 1001)
- maria (UID 1002)
- juan (UID 1003)

Usuarios en el grupo (1001):
- javi (UID 1001)
- juan (UID 1003)

Usuarios en el grupo (1002):
- maria (UID 1002)
```

---

### 💡 Sugerencia:

* Usa `split(":")` para procesar las líneas.
* Utiliza control de errores mínimo (evitar excepciones si el archivo no existe o una línea está mal formada).

---

## 📘 Ejercicio `e8.py` – Actualizar `/etc/group` a partir de `/etc/passwd`

### 📎 Apéndice introductorio:

Cambiar el GID en `/etc/passwd` **modifica la pertenencia principal del usuario**, pero **ese grupo no existe realmente** si no está definido en el archivo `/etc/group`. Por tanto, es necesario asegurarse de que cada GID asignado a un usuario tenga su correspondiente entrada en `/etc/group`, especialmente si se están simulando usuarios como parte de ejercicios en entornos como Docker.

---

### 🎯 Objetivo:

Leer la información de los usuarios definidos en `/etc/passwd` y asegurarse de que **cada GID utilizado por un usuario tiene su correspondiente grupo en `/etc/group`**. Si no existe, se añadirá una entrada simulada para ese grupo, incluyendo los miembros asociados.

---

### 🛠 Instrucciones:

1. El script debe llamarse `e8.py`.
2. Leer el archivo `/etc/passwd` y construir un diccionario `{GID: [usuarios]}` (GID, en el diccionario, son las IDs identificativas de cada grupo) solo con:

   * Usuarios con UID entre `1001` y `1999`.
   * Excluir `nobody`, `root` u otros UID especiales.
3. Leer `/etc/group` y almacenar los GIDs ya existentes.
4. Para cada GID detectado en `/etc/passwd` pero **no presente en `/etc/group`**, generar una línea nueva con formato:

```
grupo<gid>:x:GID:usuario1,usuario2,...
```

5. Añadir esas líneas al final de `/etc/group`.

---

### ✅ Requisitos técnicos:

* Validar que `/etc/group` existe antes de modificarlo.
* Hacer una copia previa del archivo con `shutil.copy()` por seguridad.
* Usar `try` / `except` para controlar errores.
* Mantener los datos originales de `/etc/group` sin alterar.

---

### 📦 Ejemplo de salida final en `/etc/group`:

Supongamos que en `/etc/passwd` tenemos:

```
javi:x:1001:1001::/home/javi:/bin/sh
maria:x:1002:1002::/home/maria:/bin/sh
juan:x:1003:1001::/home/juan:/bin/sh
```

Y que `/etc/group` no contiene los grupos `1001` ni `1002`. El script debe añadir:

```
grupo1001:x:1001:javi,juan
grupo1002:x:1002:maria
```

---

### 💡 Sugerencias:

* Usa estructuras como diccionarios para agrupar usuarios por GID.
* Al escribir en `/etc/group`, **usa `a` (append)** para no sobrescribir el archivo completo.
* Reutiliza la lógica del ejercicio 7 si fuera necesario.


