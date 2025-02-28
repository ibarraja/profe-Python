import os
import string
import random

os.system("cls")

def create_text_file(file="archivo_palabras.txt", word_count=500):
    """
    Crea un archivo con un conjunto de palabras aleatorias.
    
    Parámetros:
        file (str): Nombre del archivo a crear.
        word_count (int): Cantidad de palabras a escribir en el archivo.
    
    Devuelve:
        str: Mensaje indicando que el archivo se ha creado con éxito.
    """
    palabras = [
        "casa", "perro", "gato", "árbol", "cielo", "playa", "montaña", "libro", "mesa", "silla",
        "ventana", "sol", "luna", "estrella", "camino", "puerta", "jardín", "flor", "nube", "río",
        "ciudad", "pueblo", "auto", "tren", "avión", "barco", "bicicleta", "caminar", "correr", "saltar",
        "dormir", "soñar", "reír", "llorar", "comer", "beber", "jugar", "cantar", "bailar", "escribir",
        "leer", "pintar", "dibujar", "escuchar", "hablar", "pensar", "aprender", "enseñar", "trabajar", "viajar"
    ]

    # Generamos una lista con 500 palabras seleccionadas aleatoriamente
    palabras_aleatorias = [random.choice(palabras) for _ in range(word_count)]

    # Unimos las palabras en un solo texto
    texto = " ".join(palabras_aleatorias)

    # Guardamos en el archivo
    with open(file, 'w', encoding='utf-8') as f:
        f.write(texto)

    return f"El archivo '{file}' ha sido creado con {word_count} palabras."


def count_words(file="archivo_palabras.txt"):
    """
    Cuenta la frecuencia de las palabras en un archivo de texto.
    
    Parámetros:
        file (str): Nombre del archivo de texto.
    
    Devuelve:
        dict: Un diccionario con las palabras y su frecuencia.
    """
    try:
        with open(file, 'r', encoding='utf-8') as f:
            text = f.read()
    except FileNotFoundError:
        return '¡El fichero no existe!\n'
    
    # Eliminamos signos de puntuación y pasamos a minúsculas
    translator = str.maketrans('', '', string.punctuation)
    words = text.translate(translator).lower().split()
    
    # Contamos manualmente las palabras
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    return word_count


def show_most_common(file="archivo_palabras.txt", n=10):
    """
    Muestra las 'n' palabras más comunes del archivo.

    Parámetros:
        file (str): Nombre del archivo de texto.
        n (int): Cantidad de palabras más comunes a mostrar (por defecto 10).
    
    Devuelve:
        str: Lista de las palabras más comunes con sus frecuencias.
    """
    word_count = count_words(file)
    
    if isinstance(word_count, str):
        return word_count  # Si hay error, lo devolvemos

    # Ordenamos por frecuencia de mayor a menor
    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    
    result = "Las palabras más comunes son:\n"
    for word, freq in sorted_words[:n]:
        result += f"{word}: {freq} veces\n"

    return result


def save_word_count(file="archivo_palabras.txt", output_file="frecuencia_palabras.txt"):
    """
    Guarda la frecuencia de palabras en un archivo de salida.

    Parámetros:
        file (str): Nombre del archivo de texto.
        output_file (str): Nombre del archivo donde se guardará la información.

    Devuelve:
        str: Mensaje indicando si la operación fue exitosa o no.
    """
    word_count = count_words(file)

    if isinstance(word_count, str):
        return word_count  # Si hay error, lo devolvemos

    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            for word, freq in word_count.items():
                f.write(f"{word}: {freq}\n")
        return f"Los datos se han guardado en '{output_file}'\n"
    except Exception as e:
        return f"Error al escribir en el archivo: {e}\n"


def menu():
    """
    Muestra un menú de opciones para gestionar el contador de palabras.
    """
    # file = input("Introduce el nombre del archivo de texto a analizar: ")
    file = ""
    while True:
        print("\nMenú del Contador de Palabras")
        print("=============================")
        print("1 - Contar palabras en el archivo")
        print("2 - Mostrar las 10 palabras más comunes")
        print("3 - Guardar resultado en un archivo")
        print("4 - Crear archivo palabras random")
        print("0 - Salir")

        option = input("Elige una opción: ")
        
        if option == '1':
            file =input("[1] -> Archivo por defecto\n[nombrearchivo] -> Si tu archivo tiene un nombre personalizado\n")
            if file == "1":
                print(count_words())
            else:
                print(count_words(file))
        elif option == '2':
            file =input("[1] -> Archivo por defecto\n[nombrearchivo] -> Si tu archivo tiene un nombre personalizado\n")
            if file == "1":
                print(show_most_common())
            else:
                print(show_most_common(file))
        elif option == '3':
            file =input("[1] -> Archivo por defecto\n[nombrearchivo] -> Si tu archivo tiene un nombre personalizado\n")
            if file== "1":
                print(save_word_count())
            else:
                print(save_word_count(file))   
        elif option == '4':
            print("¿Quieres un nombre personalizado?")
            personalizar = input("[1] -> Crear el archivo con nombre por default.\n[Cualquier otra tecla] -> Crear archivo con nombre personalizado.\n")
            if personalizar == "1":
                print(create_text_file())
            else:
                print(create_text_file(input("Dime el nombre de tu archivo: ")))
        elif option == '0':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    menu()
