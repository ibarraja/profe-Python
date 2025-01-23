# Escribe una función que devuelva el producto de todos los números de una lista.
def producto_array(arr):
    producto = 1
    
    for elemento in arr:    
        producto *= elemento
    return producto

print(producto_array([1, 2, 3, 4]))  # Salida: 24