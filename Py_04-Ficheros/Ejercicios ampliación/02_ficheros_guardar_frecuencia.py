def save_word_count(word_count, file="frecuencia_palabras.txt"):
    """
    Guarda la frecuencia de palabras en un archivo.

    Parámetros:
        word_count (dict): Diccionario con palabras y su frecuencia.
        file (str): Nombre del archivo donde se guardará la información.

    Devuelve:
        str: Mensaje indicando si la operación fue exitosa o no.
    """
    with open(file, 'w', encoding='utf-8') as f:
        for word, freq in word_count.items():
            f.write(f"{word}: {freq}\n")
    
    return f"Los datos se han guardado en '{file}'"

# Prueba con un conteo de palabras
word_count = {"hola": 2, "mundo": 3, "python": 1}
print(save_word_count(word_count))
