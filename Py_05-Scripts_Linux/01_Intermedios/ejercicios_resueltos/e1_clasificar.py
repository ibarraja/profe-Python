import os, subprocess, sys
from terminal_colors import TerminalColors

subprocess.run(["clear"])


# Primer paso: comprobaremos si le hemos dado como argumento una ruta concreta
arguementos = sys.argv[1:] # Aquí capturo en una lista los posibles argumentos que haya después de '#archivo.py'

if len(arguementos) >= 1: # Si tiene uno o mas elementos significa que hemos capturado texto, entendiendo que debe de ser la ruta que queremos comprobar
    ruta = arguementos[0] 
    
    if not os.path.isdir(ruta): # comprobamos que es un ruta correcta y funcional
        print(f"{TerminalColors.BLACK_RED}❌Error: '{ruta}' no es un directorio válido.\033[0m")
else:
    ruta = os.getcwd() # Si argumentos no tiene tamaño, significa que no le hemos pasado ninguna ruta como argumento. Por lo que ruta será la ubicación actual
    

# Segundo paso: definir variables de datos que queremos almacenar:
directorios = [] # variable donde almacenaremos una lista con los nombres de directorios encontrados
archivos = [] # variable donde alamacenamos en una lista los nombres de los archivos encontrados


# Tercer paso: Obtener los elementos de la ruta:
elementos = os.listdir(ruta) # almacenamos en una lista todos los nombres de los elementos (archivos y directorios) de la ruta indicada


# Cuarto paso: clasificar los elementos según su tipo
for elemento in elementos:
    ruta_elemento = os.path.join(ruta,elemento) # Obtenemos la ruta absoluta del elemento concreto
    if os.path.isdir(ruta_elemento): # Si el elemento es un directorio lo almacenamos en la lista de directorios:
        directorios.append(elemento)
    
    elif os.path.isfile(ruta_elemento): # o si el elemento es un archivo lo almacenamos en la lista de archivos
        archivos.append(elemento)
        

# Quinto paso: mostrar la info por pantalla
print(f"\n{TerminalColors.WHITE_BLUE}📂   Directorios ({len(directorios)}): \033[0m")
for dir in directorios:
    print(f" - {dir}")

print(f"\n{TerminalColors.WHITE_GREEN}📄   Archivos ({len(archivos)}): \033[0m")
for file in archivos:
    print(f" - {file}")
    
print("")
        
        
        