velocidades = [
 82, 95, 78, 114, 90, 85, 97, 81, 73, 104, 87, 91, 80, 109, 118,
87, 79, 88, 102, 82
]

VELOCIDAD_MAXIMA_PERMITIDA = 90
SANCION_POR_KILOMETRO_EXCEDIDO = 5

contador_infractores = 0
suma_kilometros_excedidos = 0

lista_infractores = []

# 1º calular el porcentaje de conductores infractores
for i in range (0, len(velocidades)):
    if velocidades[i] > VELOCIDAD_MAXIMA_PERMITIDA:
        #Aquí calculamos el numero de infractores
        contador_infractores += 1
        
        #Aquí añadimos la velocidad de los infractores en la lista
        lista_infractores.append(velocidades[i])

porcentaje_infractores = contador_infractores*100/len(velocidades)

print(f"El porcentaje de infractores es de {porcentaje_infractores} %")


print (f"La lista de infractores es: {lista_infractores}")
