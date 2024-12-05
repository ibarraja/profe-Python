PESO_PREGUNTA = (0.75, 0.75, 1 ,1 ,1.25 ,1.50 ,2 ,1.75)

# ---------------------------------------
def pedir_datos(total_preguntas):
    calificaciones = []
    
    for i in range(1, total_preguntas+1):
        while True:
            try:
                calificacion = int(input(f'Dime tu calificación de la pregunta {i} (0..100)'))
                if 0 <= calificacion <=100:
                    calificaciones.append(calificacion)
                    break
                else:
                    print('Error: La calificaciónd debe estar entre 0 y 100.')
                    
            except:
                print('Error: Debes de ingresar un número entero válido.')
        
    return calificaciones

# ---------------------------------------
def calcular_nota_ponderada(calificaciones, ponderaciones):
    nota = 0
    
    for i in range(0,len(calificaciones)):
        nota += calificaciones[i]* ponderaciones[i]
    
    return nota/100

# ---------------------------------------
def mostrar_nota_examen(nota):
    print(f'La calificación de tu examen es {nota}')

#----------------------------------------

if __name__ == '__main__':
    calificaciones = pedir_datos(len(PESO_PREGUNTA))
    nota = calcular_nota_ponderada(calificaciones, PESO_PREGUNTA)
    mostrar_nota_examen(nota)
    
