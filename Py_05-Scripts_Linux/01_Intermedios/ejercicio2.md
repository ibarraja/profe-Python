## 🛠 Ejercicio: Crear una Carpeta en la Ruta Indicada o en el Directorio Actual

### 🎯 Objetivo:
Crear un script en Python que cree una nueva carpeta cuyo:
- **Primer argumento** es el nombre de la carpeta.
- **Segundo argumento** (opcional) es la ruta donde crearla.

Si **no se indica la ruta**, debe crear la carpeta en el **directorio actual**.

---

### 📝 Instrucciones:
1. Crea un archivo llamado `crear_carpeta_ruta.py`.
2. El script debe:
   - Comprobar que al menos se recibe **el nombre de la carpeta** como argumento.
   - Si se proporciona una ruta, usarla.
   - Si no se proporciona, usar `os.getcwd()` (el directorio actual).
3. Verificar si **ya existe una carpeta con ese nombre** en esa ruta.
   - Si existe, mostrar un mensaje de aviso.
   - Si no existe, crearla usando `subprocess.run(['mkdir', 'ruta_completa'])`.
4. Mostrar mensajes de éxito o error claros.

---

### 💡 Pistas:
- `sys.argv[1]` → nombre carpeta
- `sys.argv[2]` (opcional) → ruta
- Si no hay `sys.argv[2]`, usar `os.getcwd()`
- Usa `os.path.join()` para crear la ruta completa.
- Usa `os.path.exists()` o `os.path.isdir()` para comprobar si existe.

---

### 🧪 Ejemplos de uso:

```bash
python3 crear_carpeta_ruta.py proyecto1 /home/javier/Escritorio
```

```bash
python3 crear_carpeta_ruta.py logs
```

---

### ✅ Posibles salidas:

```
✅ Carpeta 'logs' creada en /home/javier
⚠️ Ya existe una carpeta llamada 'logs' en esa ruta.
❌ Error: Debes indicar al menos el nombre de la carpeta.
```

