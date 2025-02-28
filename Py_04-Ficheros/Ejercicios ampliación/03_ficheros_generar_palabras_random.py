import random

def create_random_text_file(file="archivo_palabras.txt", word_count=100):
    """
    Crea un archivo con palabras aleatorias.

    Parámetros:
        file (str): Nombre del archivo a crear.
        word_count (int): Número de palabras a generar.

    Devuelve:
        str: Mensaje indicando que el archivo se ha creado correctamente.
    """
    palabras = ["casa", "perro", "gato", "sol", "luna", "cielo", "río", "coche", "tren", "ciudad"]
    texto = " ".join(random.choice(palabras) for _ in range(word_count))

    with open(file, 'w', encoding='utf-8') as f:
        f.write(texto)

    return f"El archivo '{file}' ha sido creado con {word_count} palabras."

# Prueba creando un archivo con 100 palabras
print(create_random_text_file())
