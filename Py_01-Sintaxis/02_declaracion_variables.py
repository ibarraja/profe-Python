# # Declaración de variables

# a = "Python"
# b = "Aprender"
# c = "Fácil"
# d = "Sintaxis"
# e = True


# # Unir cadenas de texto
# # 1ra forma
# if e == False:
#     print (b + " " + a + " es " + c + " si se comprende su " + d)


# # 2da forma
# texto = 'Python'
# numero = '10'

# print (f'Mi mensaje es: {texto} se merece un {numero}')

# alumno1="David"
# alumno2="Ruben"
# alumno3="Pedro"
# alumno4="Silvia"

# # Diseño y multiplicaciones de cadenas
# estatura1=178
# estatura2=180
# estatura3=168
# estatura4=158

# print (f"{'Alumno':20} {'Estatura':10}")
# print (f"{'-'*20} {'-'*10}")
# print (f"{alumno1:20} {estatura1:10}")
# print (f"{alumno2:20} {estatura2:10}")
# print (f"{alumno3:20} {estatura3:10}")
# print (f"{alumno4:20} {estatura4:10}")


# #3ra forma

# texto = 'python'
# numero = 10

# print('Mi mensaje es: %s se merece un %d' % (texto, numero))

# # %s es para cadenas de texto
# # %d es para enteros
# # %f es para numeros flotantes (double)
# # %.2f es para mostrar hasta dos decimales de un flotante (cambiar numero de decimales)
# # %c es para char
# # %x es para hexadecimales
# # %o es para octales

# pi = 3.141592
# print ('Pi con dos decimales es: %.2f' % pi)

# 4ta forma funciones

texto = 'Python es un lenguaje de programación que se merece un '
numero = 10

def unirDosCadenasDeTexto(cadena1, cadena2):
    return f'{cadena1}{cadena2}'

print(unirDosCadenasDeTexto(texto,numero))