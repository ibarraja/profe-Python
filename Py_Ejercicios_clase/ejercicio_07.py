# Busca los códigos postales de las siguientes ciudades: Cáceres, Lorca, Madrid, Padrón, La Unión, Teruel, Totana, Lugo, Rueda y Santander.

# Algunas ciudades tienen varios códigos postales, usa solo uno de ellos.
# Almacena los datos en un diccionario.
# Muestra por la consola: Los códigos postales almacenados en nuestra base de datos son:
# Muestra por consola: Las ciudades que pertenecen a la comunidad murciana son: (los códigos postales de Murcia están comprendidos entre 30000 y 30999).

CODIGOS_POSTALES= {
    10001 : "Cáceres",
    30800 : "Lorca",
    28001 : "Madrid",
    15900 : "Padrón",
    30360 : "La Unión",
    44001 : "Teruel",
    30850 : "Totana",
    27001 : "Lugo",
    47490 : "Rueda",
    39001 : "Santander"
}

def mostrar_codigos_postales(cp):
    print(f'Codigos postales: {cp.keys()}')

def mostrar_ciudades_murcianas(diccionario_codigos_postales):
    print('Las ciudades murcianas son: ')
    for clave_codigo_postal in diccionario_codigos_postales:
        if 30000 < clave_codigo_postal < 31000:
            print(f'{diccionario_codigos_postales[clave_codigo_postal]}')


if __name__ == '__main__':
    # mostrar_codigos_postales(CODIGOS_POSTALES)
    mostrar_ciudades_murcianas(CODIGOS_POSTALES)