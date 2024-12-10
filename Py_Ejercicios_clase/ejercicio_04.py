import statistics

notas = [
 7, 6, 3, 9, 8, 4, 8, 2, 10, 5, 7, 5, 9, 8, 4, 1, 8, 4, 6
]

# En esta clase se han matriculado 4 alumnos nuevos. Sus notas han sido 8, 5, 4 y 9. Calcular la media de la clase teniendo en cuenta los nuevos alumnos.
# ¿Cuál ha sido la nota mas alta? ¿Y la más baja?

notas.append(8)
notas.append(5)
notas.append(4)
notas.append(9)

#Obtener la suma de las notas
suma = 0
for nota in notas:
    suma += nota

#Obtener el numero total de notas
num = 0
for nota in notas:
    num += 1
    

num=len(notas)

media_notas = suma/num
print('La media de la clase es %.2f' % media_notas)
    
#Calcular nota más alta
notaMaxima=0
for nota in notas:
    if (nota>notaMaxima):
        notaMaxima = nota
    
#Calcular nota minima
notaMinima = 10
for nota in notas:
    if(nota<notaMinima):
        notaMinima = nota


#Calcular el numero de aprobados y de suspensos

aprobado = 5
contador_aprobados = 0
contador_suspensos = 0
for nota in notas:
    if (nota >= aprobado):
        contador_aprobados = contador_aprobados + 1
    else:
        contador_suspensos += 1

print(f"Alumnos aprobados son {contador_aprobados}")
print(f"Alumnos suspensos son {contador_suspensos}")








# tupla_notas = tuple(notas)

# nota_media = statistics.mean(tupla_notas)
# nota_mas_baja = min(tupla_notas)
# nota_mas_alta = max(tupla_notas)

# print('La nota media es: %2.2f' % nota_media)
# print('La nota mas baja es: %2.2f' % nota_mas_baja)
# print('La nota mas alta es: %2.2f' % nota_mas_alta)