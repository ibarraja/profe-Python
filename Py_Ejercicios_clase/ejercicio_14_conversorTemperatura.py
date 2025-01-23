# Escribe un programa en Python que convierta temperaturas entre grados Celsius y Fahrenheit.
#  -  Implementa dos funciones:
#      1.  celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y la convierta a grados Fahrenheit.
#      2.  fahrenheit_a_celsius(fahrenheit) que reciba una temperatura en grados Fahrenheit y la convierta a grados Celsius.
#  -  El programa debe permitir al usuario elegir el tipo de conversión que desea realizar e introducir la temperatura correspondiente.

def celsius_a_fahrenheit(celsius):
    """
    Convierte una temperatura de grados Celsius a Fahrenheit.
    """
    return (celsius * 9/5) + 32

def fahrenheit_a_celsius(fahrenheit):
    """
    Convierte una temperatura de grados Fahrenheit a Celsius.
    """
    return (fahrenheit - 32) * 5/9

def mostrar_menu():
    """
    Muestra el menú y ejecuta las funciones de conversores de temperatura.
    """
    
    verdad = True
    while verdad:
        # Menú para el usuario
        print("Conversor de temperaturas")
        print("1. Convertir de Celsius a Fahrenheit")
        print("2. Convertir de Fahrenheit a Celsius")
        print("3. Salir")
    
        try:
            opcion = int(input("Elige una opción (1, 2 o 3): "))

            if opcion == 1:
                # Conversión de Celsius a Fahrenheit
                celsius = float(input("Introduce la temperatura en grados Celsius: "))
                fahrenheit = celsius_a_fahrenheit(celsius)
                for i in range(50):
                    print("")
                print(f"{celsius}°C son {fahrenheit:.2f}°F")
                print("")
                    
            elif opcion == 2:
                # Conversión de Fahrenheit a Celsius
                fahrenheit = float(input("Introduce la temperatura en grados Fahrenheit: "))
                celsius = fahrenheit_a_celsius(fahrenheit)
                for i in range(50):
                    print("")
                print(f"{fahrenheit}°F son {celsius:.2f}°C")
                print("")
            elif opcion == 3:
                print("Saliendo...")
                verdad = False
            else:
                print("Opción no válida. Por favor, elige 1, 2 o 3.")
        except ValueError as e:
            print(f"Error: {e}")    

if __name__ == "__main__":
   mostrar_menu()