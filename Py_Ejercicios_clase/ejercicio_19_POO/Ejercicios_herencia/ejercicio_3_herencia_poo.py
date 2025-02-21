# ## Ejercicio 3: Herencia Multinivel - Clasificación de Animales
# Crea una clase base `Animal` con un método `sonido()` que devuelva "Sonido genérico".

# Luego, crea una clase `Mamifero` que herede de `Animal` y tenga un método `caracteristica()` que devuelva "Es un mamífero".

# Por último, crea una clase `Gato` que herede de `Mamifero` y sobrescriba `sonido()` para devolver "Miau".

# ### **Objetivo**:
# Crea una instancia de `Gato` y prueba los métodos `sonido()` y `caracteristica()`.

class Animal:
    def sonido():
        return "Sonido genérico"
    
class Mamifero(Animal):
    def caracteristica() -> str:
        return "Es un mamífero"
    
class Gato(Mamifero):
    def sonido() -> str:
        return "Miau"
    
g = Gato()
g.sonido()
g.caracteristica()