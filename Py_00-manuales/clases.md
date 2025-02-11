# Manual Avanzado de Python: Clases

## 1. Introducción a las Clases

En Python, las clases son una herramienta fundamental de la programación orientada a objetos (OOP). Estas actúan como plantillas que permiten crear estructuras organizadas para modelar datos y comportamientos en un solo lugar. Usar clases no solo mejora la reutilización del código, sino que también facilita el diseño de sistemas robustos, escalables y mantenibles. Una vez que comprendes el concepto de clases, puedes abordar problemas complejos dividiéndolos en componentes más manejables.

### Diferencias entre Clase y Objeto

Una **clase** se puede imaginar como un plano arquitectónico que define propiedades y funcionalidades. Un **objeto**, por el contrario, es una instancia de esa clase; es decir, es la representación concreta y funcional del plano. Cada objeto tiene su propio estado, definido por sus atributos, y puede ejecutar acciones a través de métodos.

### Sintaxis Esencial

```python
class MiClase:
    """Ejemplo básico de una clase."""
    def __init__(self, atributo1, atributo2):
        self.atributo1 = atributo1
        self.atributo2 = atributo2

    def metodo(self):
        return f"Valores: {self.atributo1}, {self.atributo2}"

# Crear y usar una instancia
objeto = MiClase("Python", "Clases")
print(objeto.metodo())
```

---

## 2. Conceptos Fundamentales

### Constructor (`__init__`)

El constructor `__init__` es el primer método que se ejecuta al crear una instancia. Sirve para inicializar los atributos del objeto. A través de él, podemos configurar el estado inicial de cada instancia creada.

#### Ejemplo
```python
class Usuario:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

usuario = Usuario("Ana", 22)
print(usuario.nombre)  # Ana
```

El constructor también puede recibir valores predeterminados que se utilizan si no se proporcionan parámetros al crear una instancia.

```python
class Usuario:
    def __init__(self, nombre="Desconocido", edad=0):
        self.nombre = nombre
        self.edad = edad

usuario = Usuario()
print(usuario.nombre)  # Desconocido
```

### Atributos: Instancia y Clase

Los **atributos** son variables asociadas a una clase u objeto. 

- **De Instancia:** Únicos para cada objeto. Normalmente definidos en `__init__` y accedidos a través del prefijo `self`.
- **De Clase:** Compartidos entre todas las instancias, útiles para valores constantes o configuraciones comunes.

#### Ejemplo Avanzado
```python
class Configuracion:
    version = "1.0.0"  # Atributo de clase

    def __init__(self, usuario, permisos=[]):
        self.usuario = usuario  # Atributo de instancia
        self.permisos = permisos

    def agregar_permiso(self, permiso):
        self.permisos.append(permiso)

config = Configuracion("Admin")
config.agregar_permiso("lectura")
print(config.permisos)  # ['lectura']
```
---

### Métodos

Los métodos son funciones que definen los comportamientos de los objetos. Python categoriza los métodos en:

- **Métodos de Instancia:** Operan sobre datos únicos de una instancia y utilizan `self`.
- **Métodos de Clase:** Con el decorador `@classmethod`, permiten interactuar con atributos de clase. Usan `cls` en lugar de `self`.
- **Métodos Estáticos:** No dependen de ninguna instancia o clase y funcionan como funciones regulares dentro del contexto de la clase.

#### Ejemplo Avanzado

```python
class Herramienta:
    categoria = "Software"

    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar_categoria(self):
        return f"Categoría: {self.categoria}"

    @classmethod
    def cambiar_categoria(cls, nueva_categoria):
        cls.categoria = nueva_categoria

    @staticmethod
    def utilidad():
        return "Optimiza procesos específicos"

herramienta = Herramienta("Editor de Texto")
Herramienta.cambiar_categoria("Utilidad")
print(herramienta.mostrar_categoria())  # Categoría: Utilidad
```

Los métodos estáticos son especialmente útiles cuando no necesitamos acceso directo ni a la instancia ni a la clase, como en funciones matemáticas o validaciones.

```python
class Matematica:
    @staticmethod
    def sumar(a, b):
        return a + b

resultado = Matematica.sumar(5, 3)
print(resultado)  # 8
```

---

## 3. Herencia y Reutilización

La **herencia** es un principio fundamental de la Programación Orientada a Objetos (OOP) que permite que una clase (*hija* o *subclase*) adquiera atributos y métodos de otra clase (*padre* o *superclase*). Esto fomenta la reutilización del código, evita la redundancia y facilita la mantenibilidad del software.

### **Tipos de Herencia**

Existen varios tipos de herencia en OOP:

1. **Herencia Simple**: Una clase hija hereda de una sola clase padre.
2. **Herencia Múltiple**: Una clase hija hereda de múltiples clases padres.
3. **Herencia Multinivel**: Una clase hija hereda de otra clase hija, formando una cadena de herencia.
4. **Herencia Jerárquica**: Varias clases hijas heredan de una misma clase padre.
5. **Herencia Híbrida**: Combinación de dos o más tipos de herencia anteriores.

#### **Ejemplo de Herencia Simple**
```python
class Vehiculo:
    def __init__(self, marca):
        self.marca = marca

    def descripcion(self):
        return f"Vehículo de marca {self.marca}"

class Coche(Vehiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca)  # Llamamos al constructor de la clase padre
        self.modelo = modelo

    def descripcion(self):
        return f"Coche {self.modelo} de marca {self.marca}"

coche = Coche("Toyota", "Corolla")
print(coche.descripcion())  # Salida: Coche Corolla de marca Toyota
```

#### **Ejemplo de Herencia Múltiple**
```python
class Motor:
    def tipo_motor(self):
        return "Motor de combustión interna"

class Chasis:
    def tipo_chasis(self):
        return "Chasis monocasco"

class Automovil(Motor, Chasis):
    def descripcion(self):
        return f"Automóvil con {self.tipo_motor()} y {self.tipo_chasis()}"

auto = Automovil()
print(auto.descripcion())  # Salida: Automóvil con Motor de combustión interna y Chasis monocasco
```

#### **Ejemplo de Herencia Multinivel**
```python
class Animal:
    def sonido(self):
        return "Sonido genérico"

class Mamifero(Animal):
    def caracteristica(self):
        return "Es un mamífero"

class Perro(Mamifero):
    def sonido(self):
        return "Ladrido"

perro = Perro()
print(perro.sonido())  # Salida: Ladrido
print(perro.caracteristica())  # Salida: Es un mamífero
```

### **Ejemplo de Uso de `super()` en la Herencia**

El método `super()` se usa para llamar a métodos de la clase padre dentro de la clase hija. Esto permite extender el comportamiento de la superclase sin necesidad de reescribir código.

#### **Sin usar `super()`**
```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentacion(self):
        return f"Me llamo {self.nombre} y tengo {self.edad} años."

class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre  # Se repite la asignación de atributos de la clase padre
        self.edad = edad
        self.carrera = carrera

    def presentacion(self):
        return f"Me llamo {self.nombre}, tengo {self.edad} años y estudio {self.carrera}."

estudiante = Estudiante("Pedro", 22, "Ingeniería Informática")
print(estudiante.presentacion())
```

#### **Usando `super()`**
```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentacion(self):
        return f"Me llamo {self.nombre} y tengo {self.edad} años."

class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)  # Llamamos al constructor de la clase padre
        self.carrera = carrera

    def presentacion(self):
        return f"{super().presentacion()} Estudio {self.carrera}."

estudiante = Estudiante("Pedro", 22, "Ingeniería Informática")
print(estudiante.presentacion())  # Salida: Me llamo Pedro y tengo 22 años. Estudio Ingeniería Informática.
```

### **Diferencias entre ambas versiones**
1. **Sin `super()`**:
   - Se repiten los atributos `nombre` y `edad`, lo que genera duplicación de código.
   - Es menos flexible si la clase padre cambia, ya que habría que modificar la clase hija manualmente.

2. **Con `super()`**:
   - Se aprovecha la inicialización de la clase padre, evitando redundancias.
   - Si la clase padre cambia, la clase hija seguirá funcionando correctamente sin modificaciones adicionales.

---

## 4. Tipos de Métodos

### 📌 4.1. Métodos de Instancia

#### ✔️ Definición
Los **métodos de instancia** operan sobre una **instancia específica** de la clase. Pueden acceder y modificar los atributos de la instancia.

#### ✔️ Características:
- Siempre reciben `self` como primer parámetro.
- Pueden acceder y modificar atributos de instancia.
- Pueden llamar a otros métodos de la misma instancia.

#### ✔️ Ejemplo:
```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."

persona1 = Persona("Ana", 25)
print(persona1.saludar())  # "Hola, mi nombre es Ana y tengo 25 años."
```


### 📌 4.2. Métodos de Clase (`@classmethod`)

#### ✔️ Definición
Los **métodos de clase** operan sobre la **clase en sí misma**, en lugar de una instancia.

#### ✔️ Características:
- Se definen con `@classmethod`.
- Reciben `cls` como primer parámetro en lugar de `self`.
- Pueden modificar atributos de **clase**, pero no de instancia.
- Se pueden llamar desde la clase o desde una instancia.

#### ✔️ Ejemplo:
```python
class Coche:
    cantidad_coches = 0

    def __init__(self, marca):
        self.marca = marca
        Coche.cantidad_coches += 1

    @classmethod
    def total_coches(cls):
        return f"Se han creado {cls.cantidad_coches} coches."

c1 = Coche("Toyota")
c2 = Coche("Ford")
print(Coche.total_coches())  # "Se han creado 2 coches."
```

---

### 📌 4.3. Métodos Estáticos (`@staticmethod`)

#### ✔️ Definición
Los **métodos estáticos** son **independientes** de la clase y de las instancias. No pueden modificar ni acceder a atributos de instancia o de clase.

#### ✔️ Características:
- Se definen con `@staticmethod`.
- No reciben `self` ni `cls`.
- Funcionan como funciones normales, pero se organizan dentro de la clase.

#### ✔️ Ejemplo:
```python
class Utilidades:
    @staticmethod
    def es_par(numero):
        return numero % 2 == 0

print(Utilidades.es_par(10))  # True
print(Utilidades.es_par(7))   # False
```

---

### 📌 4.4. Métodos y Clases Abstractos

#### ✔️ Definición
En Programación Orientada a Objetos (OOP), una **clase base abstracta** es una clase que no puede ser instanciada directamente y sirve como plantilla para otras clases. Un **método abstracto** es un método definido en una clase base abstracta que debe ser implementado por las clases hijas.

Python proporciona el módulo `abc` (**Abstract Base Class**) para definir clases abstractas y métodos abstractos.

#### ✔️ Ejemplo con Clases Abstractas
```python
from abc import ABC, abstractmethod

class Dispositivo(ABC):
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    @abstractmethod
    def encender(self):
        pass

class Telefono(Dispositivo):
    def encender(self):
        return f"El teléfono {self.marca} {self.modelo} se está encendiendo."

class Portatil(Dispositivo):
    def encender(self):
        return f"El portátil {self.marca} {self.modelo} está arrancando el sistema."

# Prueba de instanciación y uso de polimorfismo
dispositivos = [
    Telefono("Samsung", "Galaxy S21"),
    Portatil("Dell", "XPS 15")
]

for dispositivo in dispositivos:
    print(dispositivo.encender())
```

#### ✔️ Explicación
1. Se define la clase abstracta `Dispositivo`, que hereda de `ABC` y tiene un método abstracto `encender()`.
2. `Telefono` y `Portatil` heredan de `Dispositivo` y deben implementar `encender()`.
3. Se crea una lista de dispositivos y se llama a `encender()` sin importar el tipo específico de objeto, demostrando **polimorfismo**.

Este enfoque es útil para representar dispositivos electrónicos que comparten una funcionalidad común, pero con comportamientos específicos según el tipo de dispositivo.

---

## 5. Polimorfismo en Programación Orientada a Objetos

El **polimorfismo** es un concepto clave en la Programación Orientada a Objetos (OOP) que permite utilizar un mismo método en diferentes clases, asegurando que cada clase implemente su propia versión del método. Esto favorece la flexibilidad y la escalabilidad del código, permitiendo que se interactúe con objetos de distintos tipos de manera uniforme.

### **Tipos de Polimorfismo**
1. **Polimorfismo de Sobreescritura (Overriding)**: Ocurre cuando una subclase redefine un método de la superclase para adaptarlo a su propio comportamiento.
2. **Polimorfismo de Sobrecarga (Overloading)**: Se da cuando múltiples métodos comparten el mismo nombre pero tienen diferentes parámetros (en Python, esto se simula con argumentos opcionales o `*args`).
3. **Polimorfismo basado en interfaces**: Ocurre cuando diferentes clases implementan los mismos métodos sin necesidad de heredar de una clase base.

### **Ejemplo de Polimorfismo por Sobreescritura**

```python
class Animal:
    def sonido(self):
        raise NotImplementedError("Este método debe ser implementado en la subclase")

class Perro(Animal):
    def sonido(self):
        return "Ladra"

class Gato(Animal):
    def sonido(self):
        return "Maúlla"

# Lista de objetos de diferentes tipos
animales = [Perro(), Gato()]

# Uso de polimorfismo: mismo método llamado en diferentes clases
for animal in animales:
    print(animal.sonido())
```

### **Ejemplo de Polimorfismo de Sobrecarga (Simulado en Python)**

Python no admite sobrecarga de métodos en el sentido estricto como en otros lenguajes (Java, C++), pero se puede lograr usando valores predeterminados o `*args`.

```python
class Calculadora:
    def suma(self, a, b, c=0):
        return a + b + c  # El tercer parámetro es opcional

calc = Calculadora()
print(calc.suma(2, 3))      # Salida: 5
print(calc.suma(2, 3, 4))   # Salida: 9
```

### **Ejemplo de Polimorfismo basado en Interfaces**

Python permite que diferentes clases implementen métodos con el mismo nombre sin necesidad de una jerarquía de herencia, lo que fomenta un polimorfismo más flexible.

```python
class Pato:
    def sonido(self):
        return "Cua cua"

class Persona:
    def sonido(self):
        return "Hola!"

# Lista de objetos sin relación de herencia
objetos = [Pato(), Persona()]

for obj in objetos:
    print(obj.sonido())  # Se ejecuta el método correspondiente a cada clase
```

### **Ventajas del Polimorfismo**
- **Facilita la extensibilidad** del código, permitiendo agregar nuevas clases sin modificar el código existente.
- **Fomenta la reutilización**, evitando duplicaciones innecesarias.
- **Promueve la flexibilidad**, permitiendo que funciones y métodos trabajen con diferentes tipos de objetos sin preocuparse de su implementación específica.
---

## 6. Encapsulación y Accesibilidad

La **encapsulación** es un principio fundamental de la Programación Orientada a Objetos (OOP) que controla cómo se accede y modifica la información de un objeto. Esto ayuda a mantener la integridad y seguridad de los datos dentro de una clase.

### **Niveles de Accesibilidad en Python**
Python utiliza convenciones de nombres para indicar diferentes niveles de accesibilidad:

- **Público**: Se puede acceder desde cualquier parte del código. No tiene prefijo especial.
- **Protegido**: Se indica con un guión bajo `_` y sugiere que solo debe usarse dentro de la clase o sus subclases.
- **Privado**: Se indica con un doble guión bajo `__` y oculta el atributo o método, evitando su acceso directo fuera de la clase.

### **Ejemplo de Encapsulación**
```python
class Datos:
    def __init__(self):
        self.publico = "Accesible"  # Atributo público
        self._protegido = "Uso interno"  # Atributo protegido
        self.__privado = "Oculto"  # Atributo privado

    def obtener_privado(self):
        return self.__privado  # Método para acceder a un atributo privado

# Creación de un objeto de la clase Datos
dato = Datos()
print(dato.publico)  # Se puede acceder libremente
print(dato._protegido)  # Se puede acceder, pero no es recomendable

# Intento de acceso directo a un atributo privado (generará un error)
# print(dato.__privado)  # AttributeError: 'Datos' object has no attribute '__privado'

# Acceso correcto a un atributo privado mediante un método
print(dato.obtener_privado())  # Salida: Oculto
```

### **Encapsulación en Métodos**
Los métodos también pueden ser públicos, protegidos o privados.
```python
class Ejemplo:
    def metodo_publico(self):
        return "Método público"
    
    def _metodo_protegido(self):
        return "Método protegido"
    
    def __metodo_privado(self):
        return "Método privado"
    
    def llamar_metodo_privado(self):
        return self.__metodo_privado()  # Acceder al método privado desde dentro de la clase

obj = Ejemplo()
print(obj.metodo_publico())  # Accesible desde cualquier parte
print(obj._metodo_protegido())  # Se puede acceder, pero no se recomienda

# print(obj.__metodo_privado())  # AttributeError
print(obj.llamar_metodo_privado())  # Correcta forma de acceder al método privado
```

### **Modificación de Atributos Privados**
En Python, aunque los atributos privados no pueden ser accedidos directamente, se pueden modificar usando métodos específicos (*getters* y *setters*).

```python
class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre  # Atributo privado
    
    def obtener_nombre(self):  # Getter
        return self.__nombre
    
    def cambiar_nombre(self, nuevo_nombre):  # Setter
        self.__nombre = nuevo_nombre

persona = Persona("Carlos")
print(persona.obtener_nombre())  # Salida: Carlos
persona.cambiar_nombre("Ana")
print(persona.obtener_nombre())  # Salida: Ana
```
---
## 7. Buenas Prácticas
1. **Nombres descriptivos:** Usa nombres que reflejen propósito.
2. **Evita dependencias circulares:** Asegura modularidad.
3. **Usa pruebas unitarias:** Verifica comportamientos esperados.
4. **Mantén la simplicidad:** No abuses de la herencia.



