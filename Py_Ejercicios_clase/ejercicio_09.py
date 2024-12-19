# Solicitar por teclado la siguiente información y almacenarla en un diccionario:

# - Nombre
# - 1er Apellido
# - 2do Apellido
# - Genero (M|F) (si no se pone M o F hay que repetir la pregunta hasta introducir una válida)
# - Fecha de nacimiento. (Tiene que ser una creible - mayores de 16, menores de 65)
# - Ciudad de nacimiento
# - País de nacimiento

# Mostrar la info preformateado el resultado del diccionario. (mínimo 3 personas)
# Tarea de matricula: exportar los datos a un JSON o un XML

def solicitar_genero():
    while True:
        try:
            genero = input("Introduce el género (M o F): ").strip().upper()
            if genero == "M" or genero =="F":
                return genero
            else:
                print(f"Error: respuesta {genero} no es correcta.")
        
        except Exception as e:
            print(f"Error inesperado: {e}")

# solicitar_genero()
            
def solicitar_fecha_nacimiento():
    year_now = 2024
    while True:
        try:
            year = int(input("Dime tu año de nacimiento: "))
            
            if year_now >= year:
                year_person = year_now - year
                
                if 66 > year_person > 15:
                    return year_person
                else:
                    if 65 < year_person:
                        print("Lo sentimos eres muy mayor. Prueba a introducir otro año de nacimiento")
                    if 15 > year_person:
                        print("Lo sentimos, eres demasiado joven. Prueba a introducir otro año de nacimiento")
            else:
                print("Error. No puedes haber nacido en el futuro...")
        except:
            print(f"Error. Introduce un año válido usando el formato YYYY. Ejemplo: 1995, 1998, 2003, etc.")

# solicitar_fecha_nacimiento()  

def solicitar_datos_persona():
    persona = {}
    persona['Nombre'] = input("Introduce el nombre: ").strip()
    persona['1er Apellido'] = input("Introduce el 1er apellido: ").strip()
    persona['2do Apellido'] = input("Introduce el 2do apellido: ").strip()
    persona['Genero'] = solicitar_genero()
    persona['Año de nacimiento'] = solicitar_fecha_nacimiento()
    persona['Ciudad de nacimiento'] = input("Introduce la ciudad de nacimiento: ").strip()
    persona['País de nacimiento'] = input("Introduce el país de nacimiento: ").strip()
    # print(persona)
    return persona

# solicitar_datos_persona()
       
def recoger_datos():
    datos=[]
    for i in range(1, 4):
        print(f"Datos de la persona {i}")
        datos.append(solicitar_datos_persona())
        # datos.append(i)
        
    print(datos)
# recoger_datos()

if __name__ == "__main__":
    recoger_datos()