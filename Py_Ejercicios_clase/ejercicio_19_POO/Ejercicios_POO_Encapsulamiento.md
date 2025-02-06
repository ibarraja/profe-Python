## Ejercicios sobre Encapsulamiento en Python

### **Ejercicio 1: Atributos Privados y Métodos Getter/Setter**
**Objetivo:** Comprender el uso de atributos privados y métodos getter y setter.

#### **Instrucciones:**  
1. Crea una clase `CuentaBancaria` con los siguientes atributos:
   - `titular` (público)
   - `__saldo` (privado)
2. Implementa los métodos:
   - `depositar(cantidad)`: Aumenta el saldo si la cantidad es positiva.
   - `retirar(cantidad)`: Reduce el saldo si la cantidad es menor o igual al saldo disponible.
   - `get_saldo()`: Retorna el saldo actual.
   - `set_saldo(nuevo_saldo)`: Permite modificar el saldo solo si el valor es mayor o igual a 0.
3. Prueba la clase creando una cuenta y manipulando el saldo con estos métodos.

---

### **Ejercicio 2: Métodos Privados**
**Objetivo:** Aplicar encapsulamiento en métodos de una clase.

#### **Instrucciones:**  
1. Crea una clase `SensorTemperatura` con los atributos:
   - `__temperatura` (privado, valor inicial 25°C)
2. Implementa los métodos:
   - `__calibrar()`: Método privado que imprime `"Calibrando sensor..."`.
   - `medir_temperatura()`: Llama a `__calibrar()` y devuelve la temperatura.
   - `set_temperatura(nueva_temp)`: Modifica la temperatura solo si está en el rango -50 a 150°C.
3. Prueba la clase instanciando un objeto y llamando a los métodos.

---

## Ejercicio 3: Encapsulamiento y Herencia en un Videojuego de Rol

### **Objetivo:**
Aplicar encapsulamiento en una clase base y heredarla en un contexto de videojuegos de rol con interacciones dinámicas.

### **Instrucciones:**

1. Crea una clase `Personaje` con:
   - `__nivel` (privado, inicializado en 1)
   - `__vida` (privado, inicializado en 100)
   - `subir_nivel()`: Aumenta el nivel en 1 y mejora la vida en 10 puntos.
   - `recibir_daño(cantidad)`: Reduce la vida si la cantidad es positiva y no deja que sea menor a 0.
   - `get_nivel()`: Retorna el nivel actual.
   - `get_vida()`: Retorna la vida actual.

2. Crea una subclase `Picaro` que tenga:
   - `__fuerza` (privado, inicializado en 10).
   - `atacar()`: Imprime "El pícaro ataca con una fuerza de X!", donde X es el valor de `__fuerza`.
   - `mejorar_fuerza()`: Aumenta la fuerza en 5 cada vez que se llama.

3. Crea una clase `Monstruo` con:
   - `__vida` (privado, inicializado en 50)
   - `recibir_daño(cantidad)`: Reduce la vida si la cantidad es positiva y no deja que sea menor a 0.
   - `get_vida()`: Retorna la vida actual.

4. Implementa un menú donde:
   - Aparezca un monstruo.
   - El jugador pueda elegir atacar al monstruo.
   - El pícaro pueda recibir daño del monstruo.
   - Se muestre la vida actual de ambos personajes tras cada acción.
   - Se pueda mejorar la fuerza del pícaro.
   - El juego termine si el pícaro o el monstruo llegan a 0 de vida.

Prueba la clase creando un `Pícaro`, subiendo de nivel, atacando, mejorando su fuerza y enfrentándose a un `Monstruo` en el menú interactivo.

---

### **Ejercicio 4: Encapsulamiento y Herencia**
**Objetivo:** Aplicar encapsulamiento en una clase base y heredarla.

#### **Instrucciones:**  
1. Crea una clase `Vehiculo` con:
   - `__velocidad` (privado, inicializado en 0)
   - `acelerar(cantidad)`: Aumenta la velocidad si la cantidad es positiva.
   - `frenar(cantidad)`: Reduce la velocidad sin que sea menor a 0.
   - `get_velocidad()`: Retorna la velocidad actual.
2. Crea una subclase `Coche` que tenga:
   - `marca` (público)
   - `__modo_sport` (privado, inicializado en `False`)
   - `activar_sport()`: Activa `__modo_sport` e imprime `"Modo Sport activado!"`.
3. Prueba la clase creando un `Coche`, acelerando, frenando y activando el modo sport.

