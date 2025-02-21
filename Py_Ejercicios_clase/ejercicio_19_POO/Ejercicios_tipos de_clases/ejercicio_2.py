# 🔹 **Ejercicio:**  
# Crea una clase `Tienda` que tenga:
# - Un atributo de clase `total_tiendas` que cuente cuántas tiendas se han creado.
# - Un constructor `__init__` que reciba el nombre de la tienda y aumente el contador de `total_tiendas`.
# - Un método de clase `cantidad_tiendas` que devuelva el número total de tiendas creadas.

# Crea varias instancias de `Tienda` y usa el método de clase para verificar cuántas tiendas hay.

class Tienda:
    total_tiendas = 0
    
    def __init__(self, name):
        self.name = name
        Tienda.total_tiendas += 1
        
    @classmethod
    def cantidad_tiendas(cls):
        return f"Se han creado {cls.total_tiendas} tiendas."
    
t1 = Tienda("Fruetería Mari")
t2 = Tienda("Mediamarkt")
t3 = Tienda("Cines Almenara")
t4 = Tienda("Cafetería El paso")
t5 = Tienda("Bar Café Zapping")

print(Tienda.cantidad_tiendas())
