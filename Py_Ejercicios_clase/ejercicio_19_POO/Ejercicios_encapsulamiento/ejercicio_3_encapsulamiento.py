# ## Ejercicio 3: Encapsulamiento y Herencia en un Videojuego de Rol

# 1. Crea una clase `Personaje` con:
#    - `__nivel` (privado, inicializado en 1)
#    - `__vida` (privado, inicializado en 100)
#    - `subir_nivel()`: Aumenta el nivel en 1 y mejora la vida en 10 puntos.
#    - `recibir_daño(cantidad)`: Reduce la vida si la cantidad es positiva y no deja que sea menor a 0.
#    - `get_nivel()`: Retorna el nivel actual.
#    - `get_vida()`: Retorna la vida actual.

# 2. Crea una subclase `Picaro` que tenga:
#    - `__fuerza` (privado, inicializado en 10).
#    - `atacar()`: Imprime "El pícaro ataca con una fuerza de X!", donde X es el valor de `__fuerza`.
#    - `mejorar_fuerza()`: Aumenta la fuerza en 5 cada vez que se llama.

# 3. Crea una clase `Monstruo` con:
#    - `__vida` (privado, inicializado en 50)
#    - `recibir_daño(cantidad)`: Reduce la vida si la cantidad es positiva y no deja que sea menor a 0.
#    - `get_vida()`: Retorna la vida actual.

# 4. Implementa un menú donde:
#    - Aparezca un monstruo.
#    - El jugador pueda elegir atacar al monstruo.
#    - El pícaro pueda recibir daño del monstruo.
#    - Se muestre la vida actual de ambos personajes tras cada acción.
#    - Se pueda mejorar la fuerza del pícaro.
#    - El juego termine si el pícaro o el monstruo llegan a 0 de vida.

# Prueba la clase creando un `Pícaro`, subiendo de nivel, atacando, mejorando su fuerza y enfrentándose a un `Monstruo` en el menú interactivo.
import time

class Personaje:
    def __init__(self):
        self.__nivel = 1
        self.__vida_max = 100
        self.__vida = 100
    
    def subir_nivel(self):
        self.__nivel += 1
        self.__vida_max += 10
        self.__vida = self.__vida_max
        
    def recibir_danio(self,cantidad):
        self.__vida -= cantidad
        
        if self.__vida < 0:
            self.muerte()
            
    def muerte(self):
        print("Personaje muere. Fin del Juego")
        
    def get_nivel(self):
        return self.__nivel
    
    def get_vida(self):
        return self.__vida
    
    def get_vida_max(self):
        return self.__vida_max

class Picaro(Personaje):
    def __init__(self):
        super().__init__()
        self.__fuerza = 10
    
    def atacar(self):
        print (f"El pícaro ataca con una fuerza de {self.__fuerza}!")
        
    def danza_espada(self):
        self.__fuerza += 4
        print(f"Pícaro subió su ataque mucho!")
        
class Monstruo:
    def __init__(self):
        self.__vida = 50
        self.__fuerza = 5
        
    def recibir_daño(self, cantidad):
        self.__vida -= cantidad
        
        if (self.__vida <= 0):
            print("El monstruo se ha debilitado")
    
    def get_vida(self):
        return self.__vida
    
    def atacar(self):
        print(f"El monstruo ataca con su palo realizando {self.__fuerza}!")

def menu():
    print("\n===== MENÚ DE JUEGO =====")
    print("1. Atacar al monstruo")
    print("2. Usar Danza de Espada")
    print("3. Ver estado del personaje")
    print("4. Salir del juego")
    
if __name__ == "__main__":
    personaje = Picaro()
    monstruo = Monstruo()
    
    print("¡Bienvenido al juego del pícaro!")
    time.sleep(1)
    
    while True:
        menu()
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            print("\nEl pícaro ataca al monstruo!")
            monstruo.recibir_daño(10)
            print(f"Vida del monstruo: {monstruo.get_vida()}")
            if monstruo.get_vida() <= 0:
                print("Has derrotado al monstruo!")
                break
            
            print("\nEl monstruo contraataca!")
            personaje.recibir_danio(5)
            print(f"Vida del pícaro: {personaje.get_vida()}")
            if personaje.get_vida() <= 0:
                print("¡El pícaro ha sido derrotado!")
                break
        
        elif opcion == "2":
            print("\nEl Pícaro uso Danza Espada!")
            personaje.danza_espada()
            print("\nEl monstruo ataca!")
            personaje.recibir_danio(5)
            print(f"Vida del pícaro: {personaje.get_vida()}")
            if personaje.get_vida() <= 0:
                print("¡El pícaro ha sido derrotado!")
                break
        
        elif opcion == "3":
            print(f"\nNivel: {personaje.get_nivel()}\nVida: {personaje.get_vida()}/{personaje.get_vida_max()}")
        
        elif opcion == "4":
            print("Saliendo del juego...")
            break
        
        else:
            print("Opción no válida, intenta de nuevo.")
        
        time.sleep(1)


    