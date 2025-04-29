## 📘 Ejercicio 3 Comprobación de comunicación con un host

### 🎯 Objetivo
Desarrollar un script en Python que permita comprobar si existe comunicación con una dirección IP mediante el comando `ping`, controlando la entrada de argumentos y capturando el resultado del proceso.

---

### 📋 Instrucciones

1. Crea un script llamado **hacer_ping_a_un_host.py**.
2. El script debe:
   - Recibir exactamente **un argumento**: una dirección IP (por ejemplo, `8.8.8.8`).
   - Verificar que se ha proporcionado **exactamente un argumento**. Si no es así, mostrar un mensaje de error y finalizar el programa con `sys.exit(1)`.
   - Utilizar `subprocess.run()` para ejecutar el comando `ping` enviando **un solo paquete** (`ping -c 1 <IP>`).
   - Capturar la salida del comando (`capture_output=True`, `text=True`).
   - Comprobar el `returncode` del comando:
     - Si el `returncode` es `0`, mostrar el mensaje **"Hay comunicación con el destino"**.
     - Si el `returncode` es distinto de `0`, mostrar **"No hay comunicación con el destino"**.

---

### 🧩 Sugerencias
- Usa `sys.argv` para recuperar los argumentos desde la línea de comandos.
- Controla correctamente los errores usando `sys.exit()` para finalizar si los argumentos no son válidos.
- Para pruebas, puedes usar direcciones como `8.8.8.8` (Google DNS) o cualquier IP de tu red local.