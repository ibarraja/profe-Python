# Escribe un programa en Python que determine si una palabra o frase es un palíndromo.
#  -  Crea una función llamada es_palindromo(cadena) que reciba una cadena de texto como parámetro y devuelva True si es un palíndromo, o False en caso contrario.
#  -  Ignora los espacios y convierte todas las letras a minúsculas para comparar correctamente.
#  -  El programa debe pedir al usuario una palabra o frase e indicar si es un palíndromo utilizando la función implementada.

def es_palindromo(cadena):
    """
    Verifica si una cadena es un palíndromo.
    """
    # Convertir todo a minúsculas y quitar espacios
    cadena_limpia = ''
    for caracter in cadena:
        if caracter.isalnum():
            cadena_limpia += caracter.lower()
    
    # Revisar si la cadena es igual al revés
    inicio = 0
    final = len(cadena_limpia) - 1
    
    while inicio < final:
        if cadena_limpia[inicio] != cadena_limpia[final]:
            return False
        inicio += 1
        final -= 1

    return True

if __name__ == "__main__":
    # Pedir al usuario una palabra o frase
    frase = input("Escribe una palabra o frase para verificar si es un palíndromo: ")

    # Usar la función y mostrar el resultado
    if es_palindromo(frase):
        print("¡Sí, es un palíndromo!")
    else:
        print("No, no es un palíndromo.")