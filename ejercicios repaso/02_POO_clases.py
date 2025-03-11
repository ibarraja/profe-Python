class Persona():
    numero_personas = 0
    
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        Persona.numero_personas += 1
        
    @classmethod
    def imprimir_num_Personas(cls):
        """Método para imprimir cuántas personas se han creado."""
        print(f"Número total de personas:{cls.numero_personas}")
    
class Alumno(Persona):
    def __init__(self,nombre, apellido, num_estudiante):
        super().__init__(nombre, apellido)
        self.num_estudiante = num_estudiante
    
    def mostrar_info(self):
        print(f"Alumno: \n  - Nombre:{self.nombre}\n  - Apellido:{self.apellido}\n  -Numero:{self.num_estudiante}")
    
    
class Profesor(Persona):
    def __init__(self,nombre, apellido, dni):
        super().__init__(nombre, apellido)
        self.dni = dni
    
        
    def mostrar_info(self):
        print(f"Profesor: \n  - Nombre:{self.nombre}\n  - Apellido:{self.apellido}\n  -Dni:{self.dni}")
    
    
# Funciones para añadir Alumnos y Profesores

def create_alumno(n, a, num):
    return Alumno(n,a,num)

def create_profe(n,a,dni):
    return Profesor(n,a,dni)

alu1 = create_alumno("David","Juarez", 123456)
alu2 = create_alumno("Sebastián","Peralta", 123457)
alu3 = create_alumno("Julio","Martínez", 123458)

alu1.mostrar_info()
alu2.mostrar_info()
alu3.mostrar_info()

profe1 = create_profe("Javier","Ibarra","22234556T")

profe1.mostrar_info()

print(Persona.numero_personas)



