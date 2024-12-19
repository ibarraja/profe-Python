# Diccionarios en Python
Un diccionario en Python es un tipo de dato compuesto que almacena pares de clave-valor. Es muy útil cuando necesitas asociar datos (clave) con valores y acceder a ellos de manera eficiente. Los diccionarios son mutables, lo que significa que puedes cambiar su contenido después de crearlos.

## 1. Características principales:
- Claves únicas: Cada clave en un diccionario debe ser única.
Tipos de claves: Las claves deben ser de un tipo inmutable, como cadenas, números o tuplas.
- Desordenados: A partir de Python 3.7, los diccionarios conservan el orden de inserción de los elementos, pero no tienen índices numéricos como las listas.

## 2. Crear un diccionario
Puedes crear un diccionario usando llaves {} o con la función dict().

```python
# Diccionario vacío
mi_diccionario = {}

# Diccionario con datos
mi_diccionario = {
    "nombre": "Javier",
    "edad": 30,
    "profesor": True
}
```
## 3. Acceder a elementos
Al contrario que en tuplas o listas que accedemos con la posicion del elemento (0...#), para acceder a los elementos en los diccionarios usamos la **clave** para acceder al **valor** asociado:

```python
print(mi_diccionario["nombre"])
```

Salida:
```makefile
Javier
```

⚠️Para evitar **errores si la clave no existe**, puedes usar el método `get`:

```python
print(mi_diccionario.get("apellido", "Clave no encontrada"))
```  

Salida:
```makefile
Clave no encontrada
```
## 3. Modificar valores
```python
mi_diccionario["edad"] = 31
print(mi_diccionario)  # Salida: {'nombre': 'Javier', 'edad': 31, 'profesor': True}
```

## 4. Agregar nuevos pares clave-valor

```python
mi_diccionario["curso"] = "DAW"
print(mi_diccionario)  # Salida: {'nombre': 'Javier', 'edad': 31, 'profesor': True, 'curso': 'DAW'}
```

## 5. Eliminar elementos
Puedes usar `del` o el `método pop`.

```python
# Usando del
del mi_diccionario["curso"]

# Usando pop
edad = mi_diccionario.pop("edad")
print(edad)  # Salida: 31
```
## 6. Métodos útiles
`keys()`: Obtiene todas las claves.
`values()`: Obtiene todos los valores.
`items()`: Obtiene pares clave-valor como tuplas.
`update()`: Actualiza el diccionario con otro.

```python
print(mi_diccionario.keys())   
print(mi_diccionario.values()) 
print(mi_diccionario.items())  
# Actualizar un diccionario
mi_diccionario.update({"curso": "DAW", "edad": 31})
print(mi_diccionario)  # Salida: 

```

```makefile
dict_keys(['nombre', 'profesor'])
dict_values(['Javier', True])
dict_items([('nombre', 'Javier'), ('profesor', True)])
{'nombre': 'Javier', 'profesor': True, 'curso': 'DAW', 'edad': 31}
```
## 7. Recorrer un diccionario
```python
for clave, valor in mi_diccionario.items():
    print(f"{clave}: {valor}")
```
Salida:
```makefile
nombre: Javier
profesor: True
curso: DAW
edad: 31
```
