# 🧙‍♂️Crear una jerarquía de personajes de  Hogwarts con métodos estáticos y ordenación utilizando clases abstractas

# Definir una clase abstraca 'Hechicero' con:
# - Atributos: 'nombre', 'casa', 'poder_magico'
# - Método abstracto: 'mostrar_info()' (para que cada sublclase lo implemente)

# Crear dos sublcases: 'Mago' y 'Bruja' que hereden de 'Hechicero' e implementen 'mostrar_info()'.
# - Mago tiene un atributo de instancia: 'escoba'
# - Bruja tiene un atributo de instancia: 'lechuza'
# Implementar método '__str__()'
# Implementar métodos 'cambiar_nombre()' y 'cambiar_casa()'
# Implementar método 'estudiar_para_examenes()' sube el 'poder_magico()' 100 puntos



from abc import ABC, abstractmethod

class Hechicero(ABC):
    def __init__(self, nombre, casa, poder_magico):
        self.nombre = nombre
        self.casa = casa
        self.poder_magico = poder_magico
        
    @abstractmethod
    def mostrar_info(self):
        pass    
    
class Mago(Hechicero):
    def __init__(self, nombre, casa, poder_magico, escoba):
        super().__init__(nombre, casa, poder_magico)
        self.escoba = escoba
        
    def mostrar_info(self):
        return f"Nombre:{self.nombre}, casa: {self.casa}, Poder Mágico: {self.poder_magico} y escoba: {self.escoba}"
    def __str__(self):
        return f"Nombre: {self.nombre} y escoba: {self.escoba}"
    
    def cambiar_nombre(self, nuevo_nombre):
         self.nombre = nuevo_nombre
         
    def cambiar_casa(self, nueva_casa):
        self.casa = nueva_casa
        
    def estudiar_para_examenes(self):
        self.poder_magico += 100
    
class Bruja(Hechicero):
    def __init__(self, nombre, casa, poder_magico, lechuza):
        super().__init__(nombre, casa, poder_magico)
        self.lechuza = lechuza
       
    def mostrar_info(self):
        return f"Nombre:{self.nombre}, casa: {self.casa}, Poder Mágico: {self.poder_magico} y lechuza: {self.lechuza}"
    
    def __str__(self):
        return f"Nombre: {self.nombre} y lechuza: {self.lechuza}"
        
    def cambiar_nombre(self, nuevo_nombre):
         self.nombre = nuevo_nombre
         
    def cambiar_casa(self, nueva_casa):
        self.casa = nueva_casa
        
    def estudiar_para_examenes(self):
        self.poder_magico += 100
        
# Añadir una clase 'UtilidadesHogwarts' con un método estático:
# - 'ordenar_por_poder(lista_hechiceros)': Ordena una lista de hechiceros por su nivel de poder mágico.
# - 'fusionar_hechiceros': Hay que pasar dos instancias de mago o bruja.Si ambos son de la misma casa sumamos el poder mágico de ambos hechiceros.Si son de dos clases distintas se suma el 75% de cada uno. 

# Probar el código con una lista de 4 magos y 5 brujas. Ordenarlos por poder mágico.

class UtilidadesHogwarts:
    @staticmethod
    def ordenar_por_poder():
       
