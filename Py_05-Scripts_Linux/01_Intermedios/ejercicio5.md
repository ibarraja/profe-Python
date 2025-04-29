## 📘 Ejercicio 5 Comprobación de comunicación con una subred

### 🎯 Objetivo
Desarrollar un script en Python que compruebe la comunicación con todos los posibles hosts de una subred dada, enviando pings secuenciales a cada dirección.

---

### 📋 Instrucciones

1. Crea un script llamado **hacer_ping_a_una_subred.py**.
2. El script debe:
   - Recibir **exactamente un argumento**: la dirección de la subred (por ejemplo, `192.168.1`).
   - Verificar que se ha proporcionado un único argumento. Si no es así, mostrar un error y finalizar el programa con `sys.exit(1)`.
   - Validar que la subred tenga el formato correcto:
     - Tres bloques numéricos separados por puntos (`.`).
     - Cada número debe estar entre `0` y `255`.
   - Para cada dirección IP de la subred (`192.168.1.1` hasta `192.168.1.254`):
     - Ejecutar un `ping` enviando **un solo paquete** (`ping -c 1 <IP>`).
     - Capturar el resultado del `ping` (`capture_output=True`, `text=True`).
     - Mostrar:
       - **"Hay comunicación con el destino \<IP\>"** si el `ping` tiene éxito (`returncode == 0`).
       - **"No hay comunicación con el destino \<IP\>"** si el `ping` falla (`returncode != 0`).

---

### 🧩 Sugerencias
- Usa bucles `for` para recorrer las direcciones IP finales del 1 al 254.
- Se recomienda crear funciones auxiliares:
  - Para validar la subred.
  - Para realizar el `ping` a un host.
- Utiliza `subprocess.run()` para lanzar el `ping` de forma controlada.
- Recuerda usar `sys.argv` para gestionar la entrada y `sys.exit()` en caso de error.