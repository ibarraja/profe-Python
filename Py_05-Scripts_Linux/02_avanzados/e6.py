import subprocess, sys

# Variables globales
ERROR_SIN_ARGUMENTOS = "⚠️ Debes indicar al menos un nombre de usuario."
ERROR_USUARIO_EXISTE = "❌ El usuario '{user}' ya existe." 

# Función para obtener el UID más alto
def obtener_uid_maximo():
    max_uid = 1000
    try:
        with open("/etc/passwd") as f:
            for linea in f:
                partes = linea.strip().split(":")
                try:
                    uid = int(partes[2])
                    if uid >= max_uid and uid != 65534:
                        max_uid = uid
                except (IndexError,ValueError):
                    continue
    except Exception as e:
        print(f"Error al leer el archivo /etc/passwd: {e}")
        sys.exit(1)

    return max_uid

# Función para comprobar si un usuario ya existe
def usuario_existe(nombre:str) -> bool:
    try:
        with open("/etc/passwd") as f:
            for linea in f:
                if linea.startswith(nombre+":"):
                    return True
            
    except Exception as e:
        print(f"Error al leer el archivo /etc/passwd: {e}")
        sys.exit(1)
    
    return False

# Programa principal
try:
    if len(sys.argv) < 2:
        raise Exception(ERROR_SIN_ARGUMENTOS)
    
    usuarios = sys.argv[1:]
    uid_actual = obtener_uid_maximo()+1
  
    for usuario in usuarios:
        try:
            if usuario_existe(usuario):
                raise Exception(ERROR_USUARIO_EXISTE.format(user = usuario))
            linea = f"{usuario}:x:{uid_actual}:{uid_actual}::/home/{usuario}:/bin/sh"
            subprocess.run(f"echo '{linea}' >> /etc/passwd", shell=True)
            print(f"✅ Usuario simulado '{usuario}' añadido con UID {uid_actual}")
            uid_actual += 1
        except Exception as e:
            print(f"Error procesando '{usuario}': {e}")
            
except Exception as e:
    print(f"{e}")
    sys.exit(1)
