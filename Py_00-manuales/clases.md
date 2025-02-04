# Manual Avanzado de Python: Clases

## Introducción a las Clases

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

## Conceptos Fundamentales

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

## Herencia y Reutilización

La **herencia** permite que una clase (*hija*) herede atributos y métodos de otra clase (*padre*). Es útil para extender funcionalidades sin duplicar código.

### **Tipos de Herencia**
- **Simple**: Una clase hereda de otra.
- **Múltiple**: Una clase hereda de varias clases.

#### **Ejemplo de Herencia Simple**
```python
class Vehiculo:
    def __init__(self, marca):
        self.marca = marca

class Coche(Vehiculo):
    def descripcion(self):
        return f"Coche de marca {self.marca}"

coche = Coche("Toyota")
print(coche.descripcion())  # Salida: Coche de marca Toyota
```

---

## Clases Abstractas y Métodos Abstractos

En Programación Orientada a Objetos (OOP), una **clase base abstracta** es una clase que no puede ser instanciada directamente y sirve como plantilla para otras clases. Un **método abstracto** es un método definido en una clase base abstracta que debe ser implementado por las clases hijas.

Python proporciona el módulo `abc` (**Abstract Base Class**) para definir clases abstractas y métodos abstractos.

### **Ejemplo con Clases Abstractas**
```python
from abc import ABC, abstractmethod
import math

class Figura(ABC):  # Clase base abstracta
    @abstractmethod
    def area(self):
        """Método abstracto que deben implementar las clases derivadas."""
        pass

class Rectangulo(Figura):  # Clase derivada concreta
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):  # Implementación obligatoria
        return self.ancho * self.alto

class Circulo(Figura):  # Otra clase derivada concreta
    def __init__(self, radio):
        self.radio = radio

    def area(self):  # Implementación obligatoria
        return math.pi * self.radio ** 2

# Prueba de instanciación y uso de polimorfismo
figuras = [Rectangulo(3, 6), Circulo(4)]
for figura in figuras:
    print(f"Área: {figura.area():.2f}")
```

### **Explicación**
1. Se define la clase abstracta `Figura`, que hereda de `ABC` y tiene un método abstracto `area()`.
2. `Rectangulo` y `Circulo` heredan de `Figura` y deben implementar `area()`.
3. Se crea una lista de figuras y se llama a `area()` sin importar el tipo específico de objeto, demostrando **polimorfismo**.

## Encapsulación y Accesibilidad
La **encapsulación** controla cómo se accede y modifica la información de un objeto. Python utiliza convenciones simples:

- Público: Sin guión bajo.
- Protegido: Prefijo `_`.
- Privado: Prefijo `__`.

```python
class Datos:
    def __init__(self):
        self.publico = "Accesible"
        self._protegido = "Uso interno"
        self.__privado = "Oculto"

    def obtener_privado(self):
        return self.__privado
```

---

## Polimorfismo
El polimorfismo permite usar métodos con el mismo nombre en diferentes clases. Esto fomenta la flexibilidad al interactuar con objetos de distintos tipos.

```python
class Animal:
    def sonido(self):
        pass

class Perro(Animal):
    def sonido(self):
        return "Ladra"

class Gato(Animal):
    def sonido(self):
        return "Maúlla"

for animal in [Perro(), Gato()]:
    print(animal.sonido())
```

---

## Buenas Prácticas
1. **Nombres descriptivos:** Usa nombres que reflejen propósito.
2. **Evita dependencias circulares:** Asegura modularidad.
3. **Usa pruebas unitarias:** Verifica comportamientos esperados.
4. **Mantén la simplicidad:** No abuses de la herencia.

---

## Conclusión
Las clases en Python son una herramienta esencial para organizar y estructurar código en proyectos complejos. Dominar conceptos como herencia, encapsulación y polimorfismo es clave para aprovechar al máximo las capacidades de la programación orientada a objetos. Este conocimiento será invaluable para desarrollar aplicaciones robustas y escalables.

