# Escribe una función que elimine los elementos duplicados de una lista.

def eliminar_duplicados(arr):
    array = []
    for elemento in arr:
        if elemento not in array:
            array.append(elemento)
        else:
            print(f"elemento {elemento} es repetido") 
            
    return array
    # return list(set(arr))
        
print(eliminar_duplicados([1, 2, 2, 3, 4, 2, 4, 5]))  # Salida: [1, 2, 3, 4, 5]


