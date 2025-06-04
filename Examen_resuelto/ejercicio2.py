import subprocess
from ejercicio1 import Conversiones 
from typing import Tuple

def obtener_ip_prefijo() -> Tuple[str, int]: 
    """
    Devuelve (IP, prefijo) a partir de `ip addr` (linea donde aparece `inet` y `scope global`).
    """
    resultado = subprocess.run(["ip", "addr"], capture_output=True, text=True)
    lineas = resultado.stdout.splitlines()
    
    for linea in lineas:
        if "inet" and "scope global" in linea:
            partes_linea = linea.split(" ")
            # print(partes_linea)
            ip_mascara = partes_linea[5]
            ip = ip_mascara.split("/")[0]
            prefijo_mascara = ip_mascara.split("/")[1]
            # print(ip)
            # print(prefijo_mascara)
            return ip, int(prefijo_mascara)
    

def obtener_mascara_desde_prefijo(prefijo: int) -> str: 
    """Convierte un prefijo en una máscara punteada. haciendo uso de un diccionario"""
    # En esta función puedes resolverlo tanto haciendo uso del siguiente diccionario:
    tabla = {8:"255.0.0.0",
            16:"255.255.0.0",
            24:"255.255.255.0",
            32:"255.255.255.255"
            }
    # return tabla[prefijo]
    
    # Como importando la función (si la has creado) del ejercicio 1 de este examen
    # Hacerlo importando tendra un extra de puntuación
    mascara_binaria = Conversiones.convertir_decimal_to_str_binaria(prefijo)
    mascara = Conversiones.convertir_str_binaria_to_str_decimal(mascara_binaria)
    return mascara

def get_broadcast() -> str: 
    """Extrae la dirección de broadcast de la misma línea de ip y máscara (cadena de texto posterior a `brd`)"""
    resultado = subprocess.run(["ip", "addr"], capture_output=True, text=True)
    lineas = resultado.stdout.splitlines()
    
    for linea in lineas:
        if "inet" and "scope global" in linea:
            partes_linea = linea.split(" ")
            broadcast = partes_linea[7]
            return broadcast

def get_gateway() -> str: 
    """Extrae la puerta de enlace con `ip route` (ip de la primera linea)."""
    resultado = subprocess.run(["ip", "route"], capture_output=True, text=True)
    lineas = resultado.stdout.splitlines()
    
    gateway = lineas[0].split(" ")[2]
    return gateway

def get_dns_servers() -> list[str]: 
    """Lee /etc/resolv.conf y extrae todas las IP tras 'nameserver'."""
    resultado = subprocess.run(["cat","/etc/resolv.conf"], capture_output=True, text=True)
    lineas = resultado.stdout.splitlines()
    
    for linea in lineas:
        if "nameserver" in linea:
            nameserver = linea.split(" ")[1]
            return nameserver
    

def main() -> None: 
    ip, prefijo = obtener_ip_prefijo()
    mascara = obtener_mascara_desde_prefijo(prefijo)
    broadcast = get_broadcast()
    gateway = get_gateway()
    nameserver = get_dns_servers()
    
    print(f"Dirección IP:           {ip}")
    print(f"Máscara de subred:      {mascara}")   
    print(f"Dirección broadcast:    {broadcast}") 
    print(f"Puerta de enlace:       {gateway}")    
    print(f"Servidores DNS:         {nameserver}")      
    
if __name__ == "__main__": 
    subprocess.run(["clear"])
    main()