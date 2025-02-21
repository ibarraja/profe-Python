class Vehiculo:
    # Atributo de clase
    tipo ="Transporte"
    
    #Atributo de instancia
    def __init__(self, marca):
        self.marca = marca
     
    # Método de clase
    @classmethod
    def obtener_tipo(cls):
        print(cls.tipo)
        # return Vehiculo.tipo
    
    def obtener_marca(self):
        return self.marca
    
    def __str__(self):
        return f"Vehiculo de marca: {self.marca}"
    
v = Vehiculo("Toyota")
print(v)

v.obtener_tipo()