# Crea una función que reciba un texto (string) y devuelva las palabras únicas ordenadas alfabéticamente, ignorando mayúsculas/minúsculas, y cuántas veces aparece cada una.

# Entrada (Ejemplo):
# texto = "Hola mundo. El mundo es increíble. Hola de nuevo."

# Salida esperada:
# {'de': 1, 'el': 1, 'es': 1, 'hola': 2, 'increíble': 1, 'mundo': 2, 'nuevo': 1}

# Crea un menú: 
#   - opción 1: la cadena de texto es un input
#   - opcion 2: la cadena de texto es una aleatoria de un Diccionario que tendreis que crear con al menos 6 frases. 

def obtener_lista_palabras(c:str):
    """
    Recoge una cadena de texto y devuelve una lista con las palabras de la frase (En esta versión permite controlar '.')
    """
    # Creo una lista con las palabras de la frase que recojo.
    lista = c.split(" ")
    print(lista)
    
    i = 0
    for item in lista:
        
        if item.endswith("."):    
            lista[i] = item[:-1]
        i += 1
    
    return lista
    
def mostrar_menu():
    """
    Muestra un menu con la información de lo que podemos hacer
    """
    
    

if __name__ == "__main__":
    mostrar_menu()
    cadena = "Hola mundo. El mundo es increíble. Hola de nuevo."
    obtener_lista_palabras(cadena)