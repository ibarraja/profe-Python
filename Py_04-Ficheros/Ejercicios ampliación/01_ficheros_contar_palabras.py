def count_words(text):
    """
    Cuenta la frecuencia de palabras en un texto.

    Parámetros:
        text (str): Texto de entrada.

    Devuelve:
        dict: Diccionario con palabras y su frecuencia.
    """
    words = text.lower().split()
    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    return word_count

# Prueba con un texto de ejemplo
text_example = "Hola mundo hola Python mundo mundo"
print(count_words(text_example))
