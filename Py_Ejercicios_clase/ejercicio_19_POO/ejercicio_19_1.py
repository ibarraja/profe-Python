class Persona:
    """Clase de una Persona"""
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad   = edad

    def saludar(self):
        return f"Hola, mi nombre es: {self.nombre} y tengo {self.edad}"

# Crear y usar una instancia
objeto = Persona("Javier", "28")
print(objeto.saludar())