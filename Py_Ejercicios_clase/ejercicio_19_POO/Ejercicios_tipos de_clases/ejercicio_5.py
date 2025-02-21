# 🔹 Ejercicio:
# Crea una clase abstracta Empleado con:

# Un método __init__ que reciba el nombre del empleado.
# Un método abstracto calcular_salario que deberá ser implementado por las clases hijas.
# Crea dos clases EmpleadoPorHora y EmpleadoFijo que hereden de Empleado:

# EmpleadoPorHora recibirá el número de horas trabajadas y la tarifa por hora, y calculará el salario multiplicando estos valores.
# EmpleadoFijo recibirá un sueldo fijo y lo devolverá como salario.
# Crea instancias de ambas clases y calcula el salario de diferentes empleados.
from abc import ABC, abstractmethod
import os

os.system("cls")

class Empleado(ABC):
    def __init__(self, nombre):
        self.nombre = nombre
    
    @abstractmethod    
    def calcular_salario(self):
        pass
    
class EmpleadoPorHora(Empleado):
    """Recibe un numero de horas fijas y la tarifa por hora. Calcula el salario"""
    
    def __init__(self, nombre, horas, tarifa):
        super().__init__(nombre)
        self.horas = horas
        self.tarifa = tarifa
        
    def calcular_salario(self):
        return self.horas * self.tarifa
    
    def __str__(self):
        return f"Empleado por horas: {self.nombre}. Su salario este mes correspondiente es de: {self.calcular_salario()}"
        
class EmpleadoFijo(Empleado):
    """Recibe un sueldo fijo y calula su salario"""
    def __init__(self, nombre, sueldo_fijo):
        super().__init__(nombre)
        self.salario = sueldo_fijo
        
    def calcular_salario(self):
        return self.salario

    def __str__(self):
        return f"Empleado asalariado: {self.nombre}. Su salario este mes correspondiente es de: {self.calcular_salario()}"
    
vendedor1 = EmpleadoPorHora("Juan", 76, 36)
vendedor2 = EmpleadoPorHora("Pedro", 86, 20)

asalariado1 = EmpleadoFijo("Javier", 2400)
asalariado2 = EmpleadoFijo("Paco", 2400)

print(vendedor1)
print(vendedor2)
print(asalariado1)
print(asalariado2)



 
        
    