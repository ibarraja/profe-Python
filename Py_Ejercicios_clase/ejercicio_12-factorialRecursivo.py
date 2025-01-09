# Ejercicio 12: Factorial Recursivo
# Enunciado:
# Escribe un programa en Python que calcule el factorial de un número entero no negativo utilizando recursividad.
#  -  Crea una función llamada factorial(n) que reciba un número entero como parámetro y devuelva su factorial.
#  -  El programa debe pedir al usuario un número entero positivo y mostrar su factorial calculado mediante la función implementada.
#  -  Asegúrate de manejar correctamente el caso base para la recursión.

def factorial(num):
    inicializador = 1
    factorial = 1
    
    for i in range(inicializador,num+1):
        factorial = factorial * i
    
    return factorial

if __name__ == "__main__":
    num = int(input("Dame un numero: "))
    print(f'El factorial de {num} es {factorial(num)}')
    
    