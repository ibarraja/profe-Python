# Escribe un programa en Python que calcule el factorial de un número entero no negativo utilizando recursividad.
#  -  Crea una función llamada factorial(n) que reciba un número entero como parámetro y devuelva su factorial.
#  -  El programa debe pedir al usuario un número entero positivo y mostrar su factorial calculado mediante la función implementada.
#  -  Un factorial, por ejemplo de 5, seria del siguiente modo:
#      - 5! = 5*4*3*2*1
#      - 0! = 1

def factorial(num):
    factorial = 1
    
    if num == 0:
        return 1
    
    for i in range(1,num+1):
        factorial = factorial * i
    
    return factorial

if __name__ == "__main__":
    try:
        num = int(input("Dame un numero: "))
        if num >= 0:
            print(f'El factorial de {num} es {factorial(num)}')
        else:
            print("El enunciado pide introducir un numero enterno no negativo.")
    except ValueError as e:
        print(f"Error: {e}")
    
