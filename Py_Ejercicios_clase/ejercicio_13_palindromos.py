# Escribe un programa en Python que determine si una palabra o frase es un palíndromo.
#  -  Crea una función llamada es_palindromo(cadena) que reciba una cadena de texto como parámetro y devuelva True si es un palíndromo, o False en caso contrario.
#  -  Ignora los espacios y convierte todas las letras a minúsculas para comparar correctamente.
#  -  El programa debe pedir al usuario una palabra o frase e indicar si es un palíndromo utilizando la función implementada.
#  -  Para transformar una cadena a minusculas: cadena.lower()
#  -  Para solo agregar caracteres alfanuméricos: cadena.isalnum()

def es_palindromo(cadena):
    cadena = cadena.lower()
    # Crear una nueva cadena sin espacios ni caracteres no alfanuméricos
    cadena_filtrada = ""
    for c in cadena:
        if c.isalnum():  # Solo agregar caracteres alfanuméricos
            cadena_filtrada += c

    # Usar punteros para comparar la cadena filtrada
    inicio = 0
    fin = len(cadena_filtrada) - 1
    
    while inicio < fin:
        print(f"{cadena_filtrada[inicio]}, {cadena_filtrada[fin]}")
        if cadena_filtrada[inicio] != cadena_filtrada[fin]:
            print(f"Discrepancia encontrada: '{cadena_filtrada[inicio]}' != '{cadena_filtrada[fin]}'")
            return False
        inicio += 1
        fin -= 1
    return True

if __name__ == "__main__":
    comprobar_palindromo = input("Escribe una cadena: ")
    if es_palindromo(comprobar_palindromo):
        print("La cadena es un palíndromo.")
    else:
        print("La cadena no es un palíndromo.")
