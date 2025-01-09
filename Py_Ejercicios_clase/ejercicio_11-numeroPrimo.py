# Ejercicio 11: Verificador de Números Primos
# Enunciado:
# Escribe un programa en Python que determine si un número entero dado es primo o no.
#  -  Crea una función llamada es_primo(numero) que reciba un número entero como parámetro y devuelva True si el número es primo, o False en caso contrario.
#  -  El programa debe pedir al usuario un número entero e indicar si es primo o no utilizando la función implementada.
#  -  Recuerda que un número primo es aquel que solo es divisible por 1 y por sí mismo.


def es_primo(num):
    contador = 1
    for i in range(num):
        contador += 1
        if num % contador == 0 and contador != num:
            return False
    return True

if __name__ == "__main__":
    num=int(input("Dame un número: "))
    if es_primo(num):
        print(f"{num} es primo")
    else:
        print(f"{num} no es primo")
        
        
    