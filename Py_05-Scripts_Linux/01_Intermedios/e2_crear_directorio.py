import os, sys, subprocess
from terminal_colors import TerminalColors

subprocess.run(['clear'])

# Primer paso: comprobaremos si le hemos dado como argumento una ruta concreta
argumentos = sys.argv[1:] # Aquí capturo en una lista los posibles argumentos que haya después de '#archivo.py'

ruta = ""
nombre_directorio = ""

if len(argumentos) >= 1 and len(argumentos) <=2: # Si tiene uno o mas elementos significa que hemos capturado texto, entendiendo que debe de ser la ruta que queremos comprobar
    nombre_directorio = argumentos[0]
    ruta = os.getcwd() # Si argumentos no tiene tamaño, significa que no le hemos pasado ninguna ruta como argumento. Por lo que ruta será la ubicación actual
    if len(argumentos) >= 2:
        ruta = argumentos[1]    
        if not os.path.isdir(ruta): # comprobamos que es un ruta correcta y funcional
            print(f"{TerminalColors.BLACK_RED}❌  Error: '{ruta}' no es un directorio válido.\033[0m")
elif len(argumentos) == 0:
    print(f"{TerminalColors.BLACK_RED}❌  Error: Debes indicar al menos el nombre de la carpeta..\033[0m")

if ruta != "" and nombre_directorio != "":
    elementos = os.listdir(ruta)
    
    directorios = []
    
    for elemento in elementos:
        ruta_completa = os.path.join(ruta,elemento)
        if os.path.isdir(ruta_completa):
            directorios.append(elemento)
    
    if nombre_directorio in directorios:
        print(f"{TerminalColors.BLACK_YELLOW}⚠️  Error: Ya existe una carpeta llamada '{nombre_directorio}' en esa ruta.\033[0m")
    
    ruta_absoluta = os.path.join(ruta, nombre_directorio)
    subprocess.run(['mkdir', ruta_absoluta])
    print(f"✅ {TerminalColors.WHITE_GREEN}  Carpeta '{nombre_directorio}' creada en {ruta}\033[0m")

    

    
    