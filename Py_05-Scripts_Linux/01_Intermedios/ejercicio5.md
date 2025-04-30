Aquí tienes el enunciado modificado según tu solicitud:

---

## 📘 Ejercicio 5 Comprobación de Disponibilidad de Hosts en una Subred

### 🎯 Objetivo
Desarrollar un script en Python que verifique qué direcciones IP en una subred están ocupadas (es decir, responden a un ping) y cuáles no responden, utilizando un tiempo de espera de 0.25 segundos.

---

### 📋 Instrucciones

1. Crea un script llamado **comprobar_disponibilidad_subred.py**.
2. El script debe:
   - Recibir **exactamente un argumento**: la dirección de la subred (por ejemplo, `192.168.1`).
   - Verificar que se ha proporcionado un único argumento. Si no es así, mostrar un error y finalizar el programa con `sys.exit(1)`.
   - Validar que la subred tenga el formato correcto:
     - Tres bloques numéricos separados por puntos (`.`).
     - Cada número debe estar entre `0` y `254`.
   - Para cada dirección IP de la subred (`192.168.1.1` hasta `192.168.1.254`):
     - Ejecutar un `ping` enviando **un solo paquete** (`ping -c 1 -W 1 <IP>`), con un tiempo de espera de 0.25 segundos.
     - Capturar el resultado del `ping` (`capture_output=True`, `text=True`).
     - Mostrar:
       - **"La dirección \<IP\> está ocupada"** si el `ping` tiene éxito (`returncode == 0`).
       - **"La dirección \<IP\> no responde"** si el `ping` falla (`returncode != 0`).

---

### 🧩 Sugerencias
- Usa bucles `for` para recorrer las direcciones IP finales del 1 al 254.
- Se recomienda crear funciones auxiliares:
  - Para validar la subred.
  - Para realizar el `ping` a un host.
- Utiliza `subprocess.run()` para lanzar el `ping` de forma controlada.
- Recuerda usar `sys.argv` para gestionar la entrada y `sys.exit()` en caso de error.
- Asegúrate de que el script maneje correctamente el timeout de 0.25 segundos para cada solicitud de ping.
