# 🔹 Ejercicio:
# Crea una clase Usuario que tenga:

# Un atributo de clase usuarios_registrados, que almacene un contador de usuarios creados.
# Un constructor que reciba el nombre del usuario e incremente usuarios_registrados.
# Un método de instancia mostrar_usuario que devuelva el nombre del usuario.
# Un método de clase cantidad_usuarios que devuelva el número total de usuarios registrados.
# Un método estático validar_nombre_usuario que reciba un nombre y devuelva True si tiene más de 3 caracteres, False en caso contrario.
# Crea varias instancias de Usuario y prueba los métodos.
import os
os.system("cls")

class Usuario:
    usuarios_registrados = 0
    
    def __init__(self, nombre_usuario):
        """Recibe un nombre de un usuario e incrementa el número de usuarios registrados"""
        self.nombre = nombre_usuario
        Usuario.usuarios_registrados +=1
        
    def mostrar_usuario(self):
        return self.nombre
    
    @classmethod
    def cantidad_usuarios(cls):
        return cls.usuarios_registrados
    
    @staticmethod
    def validar_nombre_usuario(nombre):
        if len(nombre) > 3:
            return True
        else:
            return False
        

print("Creando un usuario...")
user1 = Usuario("Perico_los_palotes")
print(f"Usuario: {user1.mostrar_usuario()}")
print(f"¿Tiene mas de tres letras el nombre del usuario? {Usuario.validar_nombre_usuario(user1.mostrar_usuario())}")
print(f"Cantidad de usuarios: {Usuario.cantidad_usuarios()}")
print()

print("Creando un usuario...")
user2 = Usuario("Pepe_Botes")
print(f"Usuario: {user2.mostrar_usuario()}")
print(f"¿Tiene mas de tres letras el nombre del usuario? {Usuario.validar_nombre_usuario(user2.mostrar_usuario())}")
print(f"Cantidad de usuarios: {Usuario.cantidad_usuarios()}")
print()


print("Creando un usuario...")
user3 = Usuario("Juana_Marrana")
print(f"Usuario: {user3.mostrar_usuario()}")
print(f"¿Tiene mas de tres letras el nombre del usuario? {Usuario.validar_nombre_usuario(user3.mostrar_usuario())}")
print(f"Cantidad de usuarios: {Usuario.cantidad_usuarios()}")
print()

print("Creando un usuario...")
user4 = Usuario("Ana")
print(f"Usuario: {user4.mostrar_usuario()}")
print(f"¿Tiene mas de tres letras el nombre del usuario? {Usuario.validar_nombre_usuario(user4.mostrar_usuario())}")
print(f"Cantidad de usuarios: {Usuario.cantidad_usuarios()}")
print()

    