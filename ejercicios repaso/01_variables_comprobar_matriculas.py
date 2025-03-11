def solicitar_matricula():
    """
    Solicita al usuario una matricula de un coche.
    Argumentos: 
        None
    Devuelve:
        Una cadena de texto
    """
    return input("Dame una matricula:")
    
def validar_matricula(m:str):
    """
    Valida si una cadena de texto cumple con el formato requerido para una matricula de un coche en España: 
    4 números enteros seguido de 3 letras mayúsculas.
    Argumentos:
        1: Una cadena de texto.
    Devuelve:
        True, si se cumplen las condiciones
        False, si no se cumplen las condiciones
    """
    # Compruebo el tamaño de la matricula sea 7
    if not len(m) == 7:
        return False
    
    validar = True
    if not m[0].isnumeric() and not m[1].isnumeric() and not m[2].isnumeric() and not m[3].isnumeric() and not m[4].isupper() and not m[5].isupper() and not m[6].isupper():
        validar = False
    return validar
    
    
if __name__ == "__main__":
    s = solicitar_matricula()
    if validar_matricula(s):
        print(f"{s} es una matricula de coche válida")
    else:
        print(f"{s} no es una matricula de coche válida")
    