# Bucles while
El bucle `While` es una estructura de control en Python que permite repetir un bloque de código mientras una condición especificada sea `True`. Es fundamental para realizar tareas repetitivas cuando no se sabe exactamente cuántas veces debe ejecutarse el código, pero sí se tiene una condición de terminación.

**Sintaxis básica:**
```python
while condición:
    # Bloque de código que se ejecuta mientras la condición sea True
```
- Condición: Es una expresión booleana que se evalúa antes de cada iteración. Si es `True`, el código dentro del bucle se ejecuta. Si es `False`, el bucle termina.
- Bloque de código: Puede contener cualquier conjunto de instrucciones.

---
## Características del bucle `while`
1. **Iteración controlada por una condición:**
   - El bucle continúa mientras la condición sea verdadera.
   - Si la condición inicial es `False`, el bucle no se ejecutará ni una sola vez.
2. **Requiere un control para evitar bucles infinitos:**
   - Si la condición nunca se vuelve `False`, el programa quedará atrapado en un bucle infinito.
3. **Se usa cuando no se conoce de antemano cuántas veces se ejecutará el bucle:**
   - A diferencia del bucle `for`, que tiene un número fijo de iteraciones, el `while` depende de una condición dinámica.

**Ejemplo básico:**
```python
contador = 0
while contador < 5:  # El bucle se ejecuta mientras contador sea menor que 5
    print(f"Contador: {contador}")
    contador += 1  # Incrementamos el contador en cada iteración
```
Salida:
```makefile
Contador: 0
Contador: 1
Contador: 2
Contador: 3
Contador: 4
```
---
## Estructura de control adicional dentro de un `while`
### 1. Uso de `break`: 
Sale del bucle inmediatamente, sin importar si la condición es `True`.

```python
contador = 0
while True:  # Bucle infinito
    if contador == 3:
        break  # Salimos del bucle si contador es 3
    print(f"Contador: {contador}")
    contador += 1
```
Salida:
```makefile
Contador: 0
Contador: 1
Contador: 2
```
Observamos que en este caso, si contador es igual a tres paramos el bucle y dejamos de imprimir datos.

### 2. Uso de  `continue`: 
Salta el resto del código en la interacción actual y pasa a la siguiente:
```python
contador = 0
while contador < 5:
    contador += 1
    if contador == 3:
        continue  # Saltamos el resto del código para esta iteración
    print(f"Contador: {contador}")
```
Salida:
```makefile
Contador: 1
Contador: 2
Contador: 4
Contador: 5
```
Observamos que en este caso, cuando contador es igual a 3, no imprime nada ya que pasa directamente a la siguiente iteración.

### 3. Uso de `else`: 
Una cláusula opcional que se ejecuta si el bucle termina de forma normal (es decir, sin un break).

```python
contador = 0
while contador < 3:
    print(f"Contador: {contador}")
    contador += 1
else:
    print("El bucle terminó de forma normal.")
```
Salida:
```makefile
Contador: 0
Contador: 1
Contador: 2
El bucle terminó de forma normal.
```
---
## Usos comunes del `while`:
### 1. Contador simple:
Se utiliza para repetir un bloque de código un número de veces, similar a un bucle for.
```python
i = 0
while i < 10:
    print(i)
    i += 1
```

### 2. Validación de entrada del usuario
Un bucle while es útil para asegurarse de que el usuario introduce una entrada válida.
```python
while True:
    try:
        edad = int(input("Introduce tu edad: "))
        if edad > 0:
            print(f"Tu edad es {edad}.")
            break
    except ValueError:
        print("Por favor, introduce un número válido.")
```

#### 2.1 `try-except`
El bloque `try-except` es una estructura de manejo de excepciones en Python que permite capturar errores en tiempo de ejecución y responder a ellos de manera controlada, evitando que el programa se interrumpa abruptamente. Es una herramienta esencial para escribir código robusto y confiable, especialmente en aplicaciones donde el usuario o el entorno pueden generar errores inesperados.

**¿Qué es una excepción?**
Una excepción es un evento que ocurre durante la ejecución de un programa y que interrumpe el flujo normal del código. Por ejemplo:
- Intentar dividir por cero: ZeroDivisionError.
- Acceder a un índice fuera de rango en una lista: IndexError.
- Convertir una cadena no válida a entero: ValueError.

Sin manejar estas excepciones, el programa se detendría y mostraría un error.

**Sintáxis básica:**
```python
try:
    # Código que puede generar una excepción
except TipoDeExcepción:
    # Código para manejar la excepción
```
- `try`: Contiene el bloque de código donde pueden ocurrir errores.
- `except`: Define cómo manejar un error específico si ocurre.

**Ejemplo básico**
```python
try:
    numero = int(input("Introduce un número: "))
    print(f"El número introducido es {numero}.")
except ValueError:
    print("Error: No has introducido un número válido.")
```
Si el usuario introduce algo que no puede convertirse en un entero, como "abc", se captura la excepción ValueError, y el programa no se detiene.

**Flujo del `try-except`**
1. Python ejecuta el código dentro del bloque `try`.
2. Si no ocurre ningún error, el bloque `except` no se ejecuta.
3. Si ocurre un error en el bloque `try`, Python busca un bloque `except` correspondiente:
   - Si encuentra un bloque que coincide con el tipo de excepción, ejecuta ese bloque.
   - Si no encuentra un manejador adecuado, el programa se detiene con un mensaje de error.

### 3. Bucle infinito controlado manualmente
El bucle continúa hasta que se encuentra una condición específica.

```python
print("Presiona 'q' para salir.")
while True:
    comando = input("Introduce un comando: ")
    if comando == "q":
        print("Saliendo del programa...")
        break
    print(f"Comando '{comando}' ejecutado.")
```

### 4. Juego de adivinanza
El usuario intenta adivinar un número hasta que acierta.

```python
numero_secreto = 7
while True:
    intento = int(input("Adivina el número secreto: "))
    if intento == numero_secreto:
        print("¡Correcto!")
        break
    elif intento < numero_secreto:
        print("El número secreto es mayor.")
    else:
        print("El número secreto es menor.")
```
--- 
## Bucles infinitos
Un bucle infinito ocurre cuando la condición del while nunca se vuelve False. Esto puede ser útil en ciertos casos, pero debe manejarse con cuidado para evitar que el programa quede atrapado.

```python
contador = 0
while True:  # Este bucle continuará para siempre
    contador +=1
    print(f"{contador} - Este es un bucle infinito. Usa las teclas 'CTRL+C' para salir.")
```

---
## Ventajas del bucle while
- Flexibilidad: Ideal cuando no se sabe cuántas iteraciones serán necesarias.
- Control dinámico: Permite manejar condiciones complejas que pueden cambiar durante la ejecución.

---
## Precauciones
- **Evitar bucles infinitos accidentales:**
- Siempre asegurarse de que la condición del `while` eventualmente se vuelva `False`.
- Si usas un contador, actualízalo dentro del bucle.
- **Control de excepciones**: Usa bloques `try-except` si el código dentro del bucle puede generar errores, especialmente cuando procesas entradas del usuario.