class Producto:
    def __init__(self, nombre, precio=0):
        self.nombre = nombre
        self.precio = precio
        
    def modificarPrecio(self,precio):
        self.precio = precio
        
    def __str__(self):
        return f"Producto: {self.nombre} - Precio: {self.precio}"
    
producto1 = Producto("Teclado")
print(producto1)

producto2 = Producto("Raton",50)
print(producto2)

producto2.modificarPrecio(30)
print(producto2)
