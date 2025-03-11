def load_data(file):
    """
    Función que devuelve la lista de datos.
    """
    try:
        #Intentamos abrir el documento y devolver la información en un array
        f = open(file, "r")
        array = f.readlines()
        f.close()
        
        lineas_devolver = []
        contador = 0
        for line in array:
            if contador >= 1:
                lineas_devolver.append(line)
            contador += 1
        
        return lineas_devolver
    
    except FileNotFoundError:
        return "Error: No se encuentra el fichero indicado"
    
def show_data(file):
    """Imprime de forma formateada los datos del documento."""
    # Llamamos a cargar datos para trabajar con la información del documento
    array = load_data(file)
    print(array)
    
    
    print("Lista usuarios:")
    # Trabajamos linea a linea para imprimir los datos de forma estética:
    for line in array:
        #Obtenemos cada uno de los elementos:
        array_linea = line.split(",")
        id = array_linea[0]
        nombre = array_linea[1]
        edad = array_linea[2]
        salario = array_linea[3]
        #Imprimimos
        print(f"ID: {id}, Nombre: {nombre}, Edad: {edad}, Salario por hora: {salario}".strip())

def look_for(file,name):
    """Devuelve la linea con la información de la persona que buscamos o un mensaje de error"""
    #Llamamos a cargar datos para trabajar con la información del documento
    array = load_data(file)
    
    # Creo una variable que inicializo en Falso. Cambia a True si se cumple la condición usuario encontrado.
    existe = False
    for line in array:
        # Mismos pasos que la función show data
        array_linea = line.split(",")
        id = array_linea[0]
        nombre = array_linea[1]
        edad = array_linea[2]
        salario = array_linea[3]
        
        # Si se encuentra un usuario con el nombre, imprimimos
        if name == nombre:
            existe = True
            print("Persona encontrada:")
            print(f"ID: {id}, Nombre: {nombre}, Edad: {edad}, Salario por hora: {salario}")
    
    if not existe:   
        print ("No existe una persona con ese nombre")

def add_data(file,user):
    """Añade al documento un nuevo campo"""
    f = open(file,"a")
    f.write(user)
    f.close()
    print("Usuario añadido")
    
def remove_user(file,id):
    """Si existe el usuario, eliminamos sus datos"""
    
    # Acceder a la información del fichero completo
    f = open(file,"r")
    array_todas_las_lineas = f.readlines()
    f.close()
    
    
    # Crear un array que queremos guardar en el fichero con todas las lineas exceptuando la que contenga el parametro id.
    array_lineas_imprimir =[]
    for line in array_todas_las_lineas:
        if not line.startswith(id):
            array_lineas_imprimir.append(line)
    
    f = open(file,"w")
    for line in array_lineas_imprimir:
        f.write(line)
    
    f.close()
            

if __name__ == "__main__":
    txt = "ejercicios repaso/datos.txt"
    # show_data(txt)
    # look_for(txt,"fdjsklñf")
    # add_data(txt,"30,Julio,58,35\n")
    remove_user(txt,"3")
    pass