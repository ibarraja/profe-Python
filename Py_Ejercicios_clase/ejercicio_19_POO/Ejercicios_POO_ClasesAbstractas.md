## Ejercicio 8: Clases abstractas y métodos abstractos
Usa el módulo `abc` para definir una clase base abstracta `Figura` con un método abstracto `area()`.

- Crea dos clases derivadas:
  - **`Rectangulo`** con atributos `ancho` y `alto`, e implementa `area()`.
  - **`Circulo`** con atributo `radio` e implementa `area()` (usa `math.pi * radio ** 2`).
  
### **Objetivo**:
Prueba creando instancias y llamando a `area()`.

---

## Ejercicio 9: Polimorfismo con listas de objetos
Extiende el ejercicio anterior y crea una lista de figuras con diferentes tipos (`Rectangulo` y `Circulo`). 

- Recorre la lista e imprime el área de cada figura usando polimorfismo.
- Comprueba que cada clase usa su implementación específica de `area()`. 

---
