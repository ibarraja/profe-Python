# Ejercicio: Gestión de Vehículos 🚗🚙

## Descripción:

Crea una clase Vehiculo que permita gestionar un conjunto de vehículos de una flota. La clase debe permitir manejar información de los vehículos y realizar conversiones de unidades de velocidad.

## Requisitos:

- Atributo de clase:

 - `cantidad_vehiculos`: Un contador que registre cuántos vehículos han sido creados.

- Constructor:

 - Debe recibir el marca del vehículo y su velocidad_kmh (velocidad en kilómetros por hora).

- Método de instancia:

  - `mostrar_info()`: Muestra la marca y la velocidad del vehículo en km/h.

- Método de clase:

  - `vehiculos_totales()`: Devuelve la cantidad total de vehículos creados.

- Método estático:

  - `convertir_millas(velocidad_kmh)`: Convierte la velocidad de km/h a millas por hora (1 km/h = 0.621371 mph).

## Casos de Prueba:

- Crea al menos tres instancias de Vehiculo con diferentes marcas y velocidades.

- Muestra la información de cada vehículo utilizando mostrar_info().

- Usa `vehiculos_totales()` para obtener cuántos vehículos han sido creados.

- Convierte la velocidad de un vehículo a millas por hora usando convertir_millas() y muestra el resultado.

## Salida esperada
```bash
Marca: Toyota | Velocidad: 120 km/h
Marca: Ford | Velocidad: 90 km/h
Marca: BMW | Velocidad: 150 km/h
Total de vehículos en la flota: 3
Velocidad de BMW en millas por hora: 93.21 mph
```
