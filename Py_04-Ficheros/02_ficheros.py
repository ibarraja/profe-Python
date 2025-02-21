## Ejercicio
# Escribir una función que pida un número entero entre 1 y 10, lea el fichero `tabla-n.txt` con la tabla de multiplicar de ese número, done `n` es el número introducido, y la muestre por pantalla. Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.


# Solicita al usuario un número entero entre 1 y 10 y lo convierte a un entero
n = int(input('Introduce un número entero entre 1 y 10: '))

# Construye el nombre del archivo que se intentará leer
nombre_fichero = 'tabla-' + str(n) + '.txt'  # Se forma el nombre del archivo en base al número ingresado

# Intenta abrir el archivo en modo lectura ("r")
try:  
    f = open(nombre_fichero, 'r')  # Abre el archivo en modo lectura
except FileNotFoundError:  # Si el archivo no existe, se captura la excepción
    print('No existe el fichero con la tabla del', n)  # Mensaje de error si el archivo no se encuentra
else:  
    print(f.read())  # Si el archivo existe, lee su contenido y lo imprime en la pantalla
    f.close()  # Cierra el archivo después de leerlo
