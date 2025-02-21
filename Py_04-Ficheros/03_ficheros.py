## Ejercicio 3
# Escribir una función que pida dos números `n` y `m` entre 1 y 10 (comprobación de errores), lea el fichero `tabla-n.txt` (si existe, en caso contrario mostrar error) con la tabla de multiplicar de ese número, y muestre por pantalla la línea m del fichero (pista: usa `f.readlines()` para almacenar en un array las lineas del documento). Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.

def get_line_from_file():
    '''
    Solicita dos valores para imprimir una línea concreta de un fichero especifico.
    Parametros:
        Vacío
    Devuelve:
        Nada. Solo  imprime
    '''        
    n = int(input('Introduce un número entero entre 1 y 10: '))
    m = int(input('Introduce otro número entero entre 1 y 10: '))
    nombre_fichero = 'tabla-' + str(n) + '.txt'

    try: 
        with open(nombre_fichero, 'r') as f:
            lineas = f.readlines()
        print(lineas[m - 1])
    except FileNotFoundError:
        print('No existe el fichero con la tabla del ', n)
    
get_line_from_file()
    
