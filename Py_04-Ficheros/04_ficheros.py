# ### **Enunciado del ejercicio: Contador de palabras en un archivo de texto desde una URL**  

# 📌 **Objetivo:**  
# Desarrollar una función en Python que reciba la URL de un archivo de texto y devuelva la cantidad de palabras contenidas en él.  

# 📌 **Instrucciones:**  
# 1. Implementa una función llamada `contar_palabras(url)` que realice lo siguiente:  
#    - Reciba como parámetro una cadena (`url`) que contenga la dirección web de un archivo de texto.  
#    - Intente acceder a la URL utilizando la biblioteca `urllib.request`.  
#    - En caso de error al acceder a la URL (por ejemplo, si el enlace no existe), debe capturar la excepción `URLError` y devolver un mensaje indicando que la URL no es válida.  
#    - Si la URL es válida, debe descargar el contenido del archivo, contar el número de palabras y devolver este valor.  
#    - Una palabra se considera cualquier conjunto de caracteres separados por espacios en blanco.  

# 2. Prueba la función llamándola con dos URLs:  
#    - Una que apunte a un archivo de texto existente, como el de *Project Gutenberg* (`https://www.gutenberg.org/files/2000/2000-0.txt`).  
#    - Otra que apunte a una URL inexistente para verificar que el programa maneja correctamente los errores.  

# 📌 **Ejemplo de salida esperada:**  
# ```python
# >>> contar_palabras('https://www.gutenberg.org/files/2000/2000-0.txt')
# 123456  # (Número de palabras en el archivo, este valor varía)

# >>> contar_palabras('https://no-existe.txt')
# '¡La url https://no-existe.txt no existe!'
# ```

# ✔️ **Requisitos adicionales:**  
# - Usa la estructura `try-except` para manejar posibles errores.  
# - Asegúrate de importar los módulos adecuados (`urllib.request` y `urllib.error`).  
# - La función debe devolver un valor numérico si el archivo existe, o un mensaje de error en caso contrario.  

# 🚀 ¡Buena suerte programando!


def contar_palabras(url):
    '''
    Función que recibe recibe la url de un fichero de texto y devuelve el número de palabras que contiene.
    Parámetros:
        url: Es una cadena con la url del fichero de texto.
    Devuelve:
        El número de palabras que contiene el fichero de texto daro por la url.
    '''
    from urllib import request
    from urllib.error import URLError
    try:
        f = request.urlopen(url)
    except URLError:
        return('¡La url ' + url + ' no existe!')
    else:
        contenido = f.read()
        return len(contenido.split())

print(contar_palabras('https://www.gutenberg.org/files/2000/2000-0.txt'))
print(contar_palabras('https://no-existe.txt'))