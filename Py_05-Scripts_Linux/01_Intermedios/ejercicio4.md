## 📘 Ejercicio 4 Comprobación avanzada de comunicación con un host

### 🎯 Objetivo
Crear un script más robusto que permita comprobar la comunicación con una dirección IP, validando la dirección suministrada y pidiéndola al usuario si no se proporciona como argumento.

---

### 📋 Instrucciones

1. Crea un script llamado **hacer_ping_a_un_host_v2.py**.
2. El script debe:
   - Permitir recibir **cero o un argumento**:
     - Si no se proporciona ningún argumento, **pedir la dirección IP** al usuario mediante `input()`.
     - Si se proporciona un argumento, usarlo como dirección IP.
     - Si se proporcionan más de un argumento, mostrar un error y finalizar el programa con `sys.exit(1)`.
   - Validar que la dirección IP tiene el formato correcto:
     - Cuatro números separados por puntos (`.`).
     - Cada número debe estar entre `0` y `255`.
   - Si la dirección IP no es válida, mostrar un error y finalizar el programa.
   - Realizar un `ping` a la dirección IP enviando **un único paquete** (`ping -c 1 <IP>`).
   - Capturar el resultado del `ping` (`capture_output=True`, `text=True`).
   - Evaluar el `returncode`:
     - Si es `0`, mostrar el mensaje **"Hay comunicación con la dirección \<IP\>"**.
     - Si es distinto de `0`, mostrar el mensaje **"No se ha podido establecer comunicación con \<IP\>"**.

---

### 🧩 Sugerencias
- Utiliza funciones auxiliares para:
  - Validar si la dirección IP es correcta.
  - Extraer la dirección IP de los argumentos o solicitarla al usuario.
- Usa `subprocess.run()` para ejecutar el `ping`.
- Emplea `sys.argv` y `sys.exit()` para gestionar los errores correctamente.
- Elimina los espacios con `strip()` si lees la IP por teclado (`input()`).
