# Calculadora con manejo de excepciones y menú interactivo
# Crea un programa en Python que simule una calculadora interactiva. El programa debe cumplir con los siguientes requisitos:

# Menú interactivo:

#   El programa debe mostrar un menú con las siguientes opciones:
#       1. Sumar dos números.
#       2. Restar dos números.
#       3. Multiplicar dos números.
#       4. Dividir dos números.
#       5. Salir del programa.

#   Entrada del usuario:
#       Los usuarios seleccionan una opción introduciendo el número correspondiente.
#       El programa debe solicitar dos números para realizar la operación seleccionada.

# Manejo de excepciones con try-except:

#   Captura los siguientes errores:
#       El usuario introduce un valor no numérico al seleccionar una opción o introducir números.
#       Intento de división por cero.
#       Selección de una opción fuera del rango permitido (1-5).

# Comportamiento del programa:
#   El programa debe continuar ejecutándose hasta que el usuario elija la opción 5 (Salir).
#   Si ocurre un error, el programa debe mostrar un mensaje adecuado y permitir al usuario intentarlo de nuevo.

def mostrar_menu():
    while True:
        print("#----------------------#")
        print("|      Calculadora     |")
        print("#----------------------#")
        print("|                      |")
        print("|     1. Suma          |")
        print("|     2. Resta         |")
        print("|     3. Producto      |")
        print("|     4. División      |")
        print("|     5. Salir         |")
        print("|                      |")
        print("#----------------------#")
            
def sumar():
   

def restar():
    
def multiplicar():
    
    
def dividir():
   
def pedir_numeros():
  
            
def desplazar_consola(repeticiones):
    for i in range(repeticiones):
        print("")
    
if __name__ == "__main__":
    mostrar_menu()
        
