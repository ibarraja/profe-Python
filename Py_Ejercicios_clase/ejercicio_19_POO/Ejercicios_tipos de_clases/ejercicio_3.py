# 🔹 **Ejercicio:**  
# Crea una clase `Numeros` que incluya:
# - Un método estático `es_primo` que reciba un número entero y devuelva `True` si es primo, `False` en caso contrario.
# - Un método estático `lista_primos` que reciba un número entero `n` y devuelva una lista con todos los números primos hasta `n`.

# Prueba los métodos sin crear una instancia de la clase.
import math

class Numeros:
    @staticmethod
    def es_primo(n):
        if n < 2:
            return False
        if n in (2, 3):
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    
    @staticmethod
    def lista_primos(n):
        if n < 2:
            return []
        
        primos = [True] * (n + 1)
        primos[0] = primos[1] = False  # 0 y 1 no son primos
        
        for i in range(2, int(n ** 0.5) + 1):
            if primos[i]:  # Si es primo, marcar sus múltiplos como no primos
                for j in range(i * i, n + 1, i):
                    primos[j] = False
        
        return [i for i in range(n + 1) if primos[i]]

# Ejemplo de uso
print(Numeros.lista_primos(50))  # Devuelve todos los primos hasta 50

        

# Ejemplo de uso
num = int(input("Introduce un número: "))
if Numeros.es_primo(num):
    print(f"¿{num} es primo?: Sí")
else:
    print(f"¿{num} es primo?: No")
    
    

    