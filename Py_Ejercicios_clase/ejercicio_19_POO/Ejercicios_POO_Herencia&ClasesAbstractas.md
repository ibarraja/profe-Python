## Ejercicio 1: Gestión de empleados
Crea una clase base llamada `Empleado` con los siguientes atributos y métodos:

- **Atributos**:
  - `nombre` (str)
  - `salario` (float)

- **Métodos**:
  - `mostrar_info()`: Debe imprimir `"Empleado: [nombre], Salario: [salario]"`.
  - `calcular_bono()`: Devuelve el **10% del salario**.

Luego, crea dos clases derivadas:

- **`Gerente`**:
  - Sobrescribe `calcular_bono()` para devolver el **20% del salario**.
  
- **`Desarrollador`**:
  - Sobrescribe `calcular_bono()` para devolver el **15% del salario**.
  
### **Objetivo**:  
Crea instancias de `Gerente` y `Desarrollador` y muestra su información junto con el bono calculado.

---

## Ejercicio 2: Sistema de personajes en un juego
Crea una clase base llamada `Personaje` con los siguientes atributos y métodos:

- **Atributos**:
  - `nombre` (str)
  - `vida` (int)

- **Métodos**:
  - `atacar()`: Imprime `"El personaje ataca"`.
  - `recibir_danio(puntos)`: Resta `puntos` a `vida` e imprime `"Vida restante: [vida]"`.

Luego, crea dos clases derivadas:

- **`Guerrero`**:
  - Sobrescribe `atacar()` para imprimir `"El Guerrero golpea con su espada!"`.

- **`Mago`**:
  - Sobrescribe `atacar()` para imprimir `"El Mago lanza un hechizo!"`.

### **Objetivo**:  
Crea instancias de `Guerrero` y `Mago`, haz que ataquen y que reciban daño.

---

## Ejercicio 3: Clases con métodos adicionales
Crea una clase `Vehiculo` con los atributos:

- `marca` (str)
- `modelo` (str)
- `velocidad_maxima` (int)

Y los métodos:
- `detalles()`: Imprime la información del vehículo.
- `acelerar()`: Imprime `"El vehículo está acelerando"`.

Luego, crea dos clases derivadas:

- **`Coche`**: Agrega un atributo adicional `tipo_combustible` y sobrescribe `acelerar()` para imprimir `"El coche está acelerando rápidamente"`.
- **`Bicicleta`**: Agrega un atributo `tipo` (por ejemplo, "montaña" o "ciudad") y sobrescribe `acelerar()` para imprimir `"La bicicleta está tomando velocidad"`.

### **Objetivo**:
Instancia objetos y prueba los métodos.

---

## Ejercicio 4: Clases abstractas y métodos abstractos
Usa el módulo `abc` para definir una clase base abstracta `Figura` con un método abstracto `area()`.

- Crea dos clases derivadas:
  - **`Rectangulo`** con atributos `ancho` y `alto`, e implementa `area()`.
  - **`Circulo`** con atributo `radio` e implementa `area()` (usa `math.pi * radio ** 2`).
  
### **Objetivo**:
Prueba creando instancias y llamando a `area()`.

---

## Ejercicio 5: Polimorfismo con listas de objetos
Extiende el ejercicio anterior y crea una lista de figuras con diferentes tipos (`Rectangulo` y `Circulo`). 

- Recorre la lista e imprime el área de cada figura usando polimorfismo.
- Comprueba que cada clase usa su implementación específica de `area()`. 

---

Estos ejercicios ayudan a reforzar la comprensión de **herencia, sobrescritura de métodos y polimorfismo** en Python. 🚀
