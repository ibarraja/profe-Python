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
                
        try:
            valor = int(input("¿Qué quieres hacer? "))
            if valor == 1:
                sumar()
                desplazar_consola(4)
            elif valor == 2:
                restar()
                desplazar_consola(4)
            elif valor == 3:
                multiplicar()
                desplazar_consola(4)
            elif valor == 4:
                dividir()
                desplazar_consola(4)
            elif valor == 5:
                print("#############################################")
                print("|       Hasta pronto, gracias por todo      |")
                print("#############################################")
                return
            else:
                print("#############################################")
                print("|   Error: Selección fuera del rango (1-5)  |")
                print("#############################################")
                
        except ValueError:
            print("#############################################")
            print("| Error: no has introducido un valor válido |")
            print("#############################################")

def sumar():
    numeros = pedir_numeros()
    suma = numeros[0]+numeros[1]
    desplazar_consola(50)
    print("##################################################")
    print("#                                                #")
    print(f"La suma de {numeros[0]} y {numeros[1]} es {suma}")
    print("#                                                #")
    print("##################################################")

def restar():
    numeros = pedir_numeros()
    resta = numeros[0]-numeros[1]
    desplazar_consola(50)
    print("##################################################")
    print("#                                                #")
    print(f"La resta de {numeros[0]} y {numeros[1]} es {resta}")
    print("#                                                #")
    print("##################################################")

def multiplicar():
    numeros = pedir_numeros()
    producto = numeros[0]*numeros[1]
    desplazar_consola(50)
    print("##################################################")
    print("#                                                #")
    print(f"La multiplicación de {numeros[0]} y {numeros[1]} es {producto}")
    print("#                                                #")
    print("##################################################")
    

def dividir():
    numeros = pedir_numeros()
    dividendo=numeros[0]
    divisor=numeros[1]
    
    if(divisor==0):
        while divisor==0:
            print("##################################################")
            print("|        Error. No puedo dividir por cero.       |")
            print("##################################################")
            try:
                divi = int(input("Por favor, introduce otro número que no sea cero"))
                if divi != 0:
                    divisor = divi
            except:
                print("##################################################")
                print("|       Error. Introduce un número válido.       |")
                print("##################################################")
                
    
                
    division = dividendo/divisor
    desplazar_consola(50)
    print("##################################################")
    print("#                                                #")
    print(f"La división de {dividendo} y {divisor} es {division}")
    print("#                                                #")
    print("##################################################")
    
    
def pedir_numeros():
    numeros = []
    while True:
        try:
            num1 = int(input("Dame un primer valor "))
            numeros.append(num1)
            num2 = int(input("Dame un segundo valor "))
            numeros.append(num2)
            return numeros
        except:
            print("Error. Me tienes que dar dos números válidos")
            
def desplazar_consola(repeticiones):
    for i in range(repeticiones):
        print("")
    
if __name__ == "__main__":
    mostrar_menu()
        