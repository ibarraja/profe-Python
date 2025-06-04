from typing import Tuple
import subprocess, sys

CANTIDAD_MAXIMA_INFORMES = 30
ERROR_RECUPERANDO_ARGUMENTOS = 1
ERROR_GENERANDO_FICHEROS = 2

def main():
    """
    Qué hace: Controla la ejecución principal del script.
    - Limpia la pantalla.
    - Extrae argumentos del script.
    - Llama a la función que genera los ficheros.

    Qué devuelve: Nada (es el punto de entrada del script).
    """
    limpiar_pantalla()
    argumentos = sys.argv[1:]
    try:
        nombre, num_ficheros = extraer_nombre_cantidad_informes(argumentos)
        generar_ficheros_informes(nombre, num_ficheros)
    except Exception as e:
        print(f"ERROR > {e}")

def limpiar_pantalla():
    """
    Qué hace: Ejecuta el comando 'clear' para limpiar la pantalla del terminal.
    Qué devuelve: Nada.
    """
    subprocess.run(["clear"])

def extraer_nombre_cantidad_informes(argumentos) -> Tuple[str,int]:
    """
    Qué hace: Valida y extrae los argumentos pasados al script.
    - El primero es el nombre base del fichero.
    - El segundo es la cantidad de informes a generar (máximo permitido).

    Qué devuelve: Una tupla con (nombre, cantidad).
    """
    # Validación de tamaño arguemntos
    nombre = argumentos[0]
    num_informes = int(argumentos[1])
    if len(argumentos) < 2:
        raise Exception("Cantidad de argumentos incorrecta")
    elif not nombre.endswith(".docx"):
        raise Exception("El nombre no es válido")
    elif num_informes > CANTIDAD_MAXIMA_INFORMES or num_informes <= 0:
        raise Exception("El número de informes no es válido")
    else:
        return nombre, num_informes
    

def generar_ficheros_informes(nombre_informe, cantidad_informes) -> None:
    """
    Qué hace: Genera ficheros de informe solo en días laborables, a partir de mañana.
    Qué devuelve: Nada. Crea archivos en el sistema.
    """
    dia_actual = obtener_dia_actual()
    mes_actual = obtener_mes_actual()
    año_actual = obtener_año_actual()

    # AAAA-MM-DD-dia_semana-nombre_base.docx 
    # Bucle que copia los archivos.
    for i in range(cantidad_informes):
        i+=1
        fecha = calcular_fecha_futura(dia_actual, mes_actual, año_actual, i)
        dia_semana = obtener_dia_semana_letra(fecha)
        nombre_fichero = f"{fecha}-{dia_semana}-{nombre_informe}"
        copiar_fichero(nombre_fichero)
    

def calcular_fecha_futura(dia_actual: int, mes_actual: int, año_actual: int, dias_pasados: int) -> str:
    """
    Qué hace: Calcula la fecha futura en formato AAAA-MM-DD, ajustando el cambio de mes.
    Qué devuelve: Una cadena con la fecha futura.
    """
    # Si al no nos pasamos del mes de junio
    if dia_actual + dias_pasados <= 30:
        dia_fichero = dia_actual + dias_pasados
        mes_fichero = mes_actual
    else:   
        dia_fichero = (dia_actual + dias_pasados) - 30
        mes_fichero = mes_actual + 1

    # Si el dia_actual es menor de 10 añadir un '0' delante al dia_fichero
    if dia_fichero < 10:
        dia_fichero = "0"+str(dia_fichero)
    if mes_fichero < 10:
        mes_fichero = "0"+str(mes_fichero)
    
    cadena_fecha = f"{año_actual}-{mes_fichero}-{dia_fichero}"
    return cadena_fecha

def copiar_fichero(nombre):
    """
    Qué hace: Crea un nuevo fichero copiando 'plantilla.docx' con el nombre especificado.
    Qué devuelve: Nada. Lanza excepción si falla.
    """
    resultado = subprocess.run(["cp","plantilla.docx",f"{nombre}"], text = True, capture_output= True)
    if resultado.returncode != 0:
        raise Exception(f"No se ha podido crear el fichero {nombre}")
    else: 
        print(f"Archivo > `{nombre}` creado correctamente!")

def obtener_dia_actual() -> int:
    """
    Qué hace: Obtiene el día actual del mes.
    Qué devuelve: Entero entre 1 y 30.
    """
    resultado = subprocess.run(["date","+%d"],capture_output=True, text=True)
    if resultado.returncode != 0:
        raise Exception("No se ha podido recuperar el dia correctamente")
    else:
        dia = int(resultado.stdout)
        return dia

def obtener_mes_actual() -> int:
    """
    Qué hace: Obtiene el mes actual.
    Qué devuelve: Entero entre 1 y 12.
    """
    resultado = subprocess.run(["date","+%m"],capture_output=True, text=True)
    if resultado.returncode != 0:
        raise Exception("No se ha podido recuperar el mes correctamente")
    else:
        dia = int(resultado.stdout)
        return dia

def obtener_año_actual() -> int:
    """
    Qué hace: Obtiene el año actual.
    Qué devuelve: Año actual como entero (ej: 2025).
    """
    resultado = subprocess.run(["date","+%Y"],capture_output=True, text=True)
    if resultado.returncode != 0:
        raise Exception("No se ha podido recuperar el año correctamente")
    else:
        dia = int(resultado.stdout)
        return dia

def obtener_dia_semana_letra(fecha) -> str:
    """
    Qué hace: Obtiene el nombre del día de la semana (lunes, martes, ...).
    Qué devuelve: Cadena con el nombre del día.
    """
    resultado = subprocess.run(["date","+%a",f"--date={fecha}"],capture_output=True, text=True)
    if resultado.returncode != 0:
        raise Exception("No se ha podido recuperar el dia escrito correctamente")
    else:
        dia_en_ingles = resultado.stdout.strip()
        if dia_en_ingles == "Mon":
            return "Lunes"
        elif dia_en_ingles == "Tue":
            return "Martes"
        elif dia_en_ingles == "Wed":
            return "Miercoles"
        elif dia_en_ingles == "Thu":
            return "Jueves"
        elif dia_en_ingles == "Fri":
            return "Viernes"
        elif dia_en_ingles == "Sat":
            return "Sábado"
        elif dia_en_ingles == "Sun":
            return "Domingo"
    
    
    

def es_dia_laborable(fecha) -> bool:
    """
    Qué hace: Determina si una fecha es laborable (lunes a viernes).
    Qué devuelve: True si lo es, False si es fin de semana.
    """

if __name__ == "__main__":
    main()