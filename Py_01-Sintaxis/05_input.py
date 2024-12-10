# Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error

dividendo = int(input('Introduce el dividendo: '))
divisor = int(input('Dame el divisor: '))

if (divisor == 0):
    print ('ERROR: En matemáticas no se puede dividir por cero.')
else:
    cociente = dividendo/divisor
    print('El resultado es '+ str(cociente))

