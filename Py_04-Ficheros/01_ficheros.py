## Ejercicio:

# Escribir una función que pida un número entero entre 1 y 10 y guarde en un fichero con el nombre `tabla-n.txt` la tabla de multiplcar de ese número, donde `n` es el múmero introducido.

# Solicita al usuario un número entero entre 1 y 10 y lo convierte a un entero
n = int(input('Introduce un número entero entre 1 y 10: '))

# Construye el nombre del archivo donde se guardará la tabla de multiplicar
nombre_fichero = 'tabla-' + str(n) + '.txt'

# Abre el archivo en modo escritura ("w"), lo que sobrescribirá el contenido si el archivo ya existe
f = open(nombre_fichero, "w")

# Bucle que genera la tabla de multiplicar del número ingresado
for i in range (1, 11):
    # Crea una línea con la multiplicación en formato "n x i = resultado"
    print(str(n) + ' x ' + str(i) + ' = ' + str(n * i) + "\n")  # Muestra el resultado en pantalla
    f.write(str(n) + ' x ' + str(i) + ' = ' + str(n * i) + "\n")  # Escribe la misma línea en el archivo

# Cierra el archivo para asegurar que los cambios se guarden correctamente
f.close()
