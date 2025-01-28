# Ejercicios de Programación Orientada a Objetos en Python

## Ejercicio 1: Crear una Clase Simple
Crea una clase llamada `Persona` con los atributos `nombre` y `edad`. Añade un método llamado `saludar` que devuelva un mensaje en el formato:

> "Hola, mi nombre es [nombre] y tengo [edad] años".

Prueba la clase creando una instancia y llamando al método.

---

## Ejercicio 2: Constructor con Valores Predeterminados
Crea una clase `Producto` con un constructor que acepte dos parámetros: `nombre` y `precio`, donde `precio` tenga un valor predeterminado de `0`. Añade un método que permita modificar el precio del producto. 

Prueba creando un objeto sin especificar el precio y otro especificándolo, mostrando los resultados.

---

## Ejercicio 3: Atributos de Clase e Instancia
Define una clase `Vehiculo` que tenga un atributo de clase `tipo` con el valor "Transporte". El constructor debe aceptar un parámetro `marca` y asignarlo como atributo de instancia. 

Crea un método que devuelva el tipo y la marca del vehículo.

---

## Ejercicio 4: Métodos de Clase y Métodos Estáticos
Crea una clase `Banco` con un atributo de clase `tasa_interes` inicializado a `0.05`.

1. Define un método de clase que permita actualizar la tasa de interés.
2. Añade un método estático llamado `convertir_moneda` que reciba un valor en dólares y lo convierta a euros (asume una tasa fija de `0.85`).

Prueba la clase actualizando la tasa de interés y utilizando el método estático.

---

## Ejercicio 5: Herencia y Sobrescritura
Define una clase base `Animal` con un método `hacer_sonido` que imprima:

> "El animal hace un sonido".

Crea dos clases hijas, `Perro` y `Gato`, que sobrescriban el método `hacer_sonido` con:

- "El perro ladra".
- "El gato maúlla".

Crea una lista de objetos de ambas clases y recorre la lista llamando al método `hacer_sonido`.

---

## Ejercicio 6: Encapsulación
Crea una clase `CuentaBancaria` con un atributo privado `__saldo` y métodos para:

1. Depositar una cantidad, sumándola al saldo.
2. Retirar una cantidad si hay suficiente saldo; de lo contrario, imprime un mensaje indicando que no hay fondos suficientes.
3. Consultar el saldo mediante un método público.

Prueba las operaciones de depósito, retiro y consulta.

---

## Ejercicio 7: Validaciones con Métodos Estáticos
Crea una clase `Validador` que incluya:

1. Un método estático `es_numero_positivo` que reciba un número y devuelva `True` si es positivo, o `False` en caso contrario.
2. Un método estático `es_cadena_valida` que reciba un string y devuelva `True` si tiene más de 3 caracteres, o `False` en caso contrario.

Prueba los métodos con diferentes valores.

---

## Ejercicio 8: Creación de un Sistema de Configuración
Crea una clase `Configuracion` con:

1. Un atributo de clase `version` con valor "1.0".
2. Un constructor que reciba el nombre del usuario y una lista de permisos.
3. Métodos para agregar y eliminar permisos de la lista.
4. Un método de clase que permita cambiar la versión global de la configuración.

Prueba creando instancias y manipulando los permisos.
