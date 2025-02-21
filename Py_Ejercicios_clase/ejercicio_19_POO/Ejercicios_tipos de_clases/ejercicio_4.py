# 🔹 **Ejercicio:**  
# Crea una clase `Vehiculo` que tenga:
# - Un atributo de clase `total_vehiculos` que almacene cuántos vehículos han sido creados.
# - Un constructor que reciba el modelo y el año de fabricación del vehículo, almacenándolo como un atributo de instancia, e incremente `total_vehiculos`.
# - Un método de instancia `detalles` que devuelva la información del vehículo.
# - Un método de clase `contar_vehiculos` que devuelva cuántos vehículos existen.
# - Un método estático `es_vehiculo_moderno` que reciba una instancia de `Vehiculo` y devuelva `True` si su atributo `año_fabricacion` es del 2015 en adelante, `False` en caso contrario.

# Crea varias instancias de `Vehiculo` y verifica el uso correcto de los métodos.

class Vehiculo:
    total_vehiculos = 0
    
    def __init__(self, modelo, anio):
        self.modelo = modelo
        self.anio = anio
        Vehiculo.total_vehiculos += 1
        
    def detalles(self):
        return f"Vehiculo-> Modelo: {self.modelo}, Año: {self.anio}"
    
    @classmethod
    def contar_vehiculos(cls):
        return cls.total_vehiculos
    
    @staticmethod
    def es_vehiculo_moderno(v):
        if v.anio >= 2015:
            return True
        else:
            return False
        
vehiculo1 = Vehiculo("Toyota Corolla", 2010)
vehiculo2 = Vehiculo("Honda Civic", 2018)
vehiculo3 = Vehiculo("Ford Focus", 2022)

print(vehiculo1.detalles())  
print(vehiculo2.detalles())  
print(vehiculo3.detalles())

print(Vehiculo.es_vehiculo_moderno(vehiculo1))  
print(Vehiculo.es_vehiculo_moderno(vehiculo2))  
print(Vehiculo.es_vehiculo_moderno(vehiculo3))  

print(Vehiculo.contar_vehiculos())