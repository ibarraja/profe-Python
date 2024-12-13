# Almacena la siguiente información sobre los álbumes más vendidos en los años 90 en una lista de diccionarios (menos mal que no existía el Reggaeton):
# Recuerda que cada álbum es un array de diccionarios (year, artist o grupo, album, sold y country)

# Muestra por consola:
#   - El disco más vendido fue XXX del artista YYY que vendió ZZZ álbumes
#   - El disco más vendido en Reino Unido fue XXX en el año YYY
#   - El disco Estrella de mar vendió XXX álbumes en el año YYY
#   - El disco no español más vendido fue XXX del artista YYY
#   - El álbum en español más vendido en la segunda mitad de la década de los 90 fue XXX del artista YYY
#   - Los álbumes más vendidos cada año fueron:

ALBUMES= [
    {"year":1993, "artist":"Gloria Estefan",        "album": "Mi tierra",               "sold":1000000, "country":"Cuba"},
    {"year":1993, "artist":"Laura Pausini",         "album": "Laura Pausini",           "sold":1350000, "country":"Italia"},
    {"year":1991, "artist":"Juan Luis",             "album": "Guerra Bachata Rosa",     "sold":700000,  "country":"República Dominicana"},
    {"year":2002, "artist":"Operación Triunfo",     "album": "Álbum",                   "sold":1200000, "country":"España"},
    {"year":1996, "artist":"Spice Girls",           "album": "Spice",                   "sold":1000000, "country":"Reino Unido"},
    {"year":2000, "artist":"La Oreja de Van Gogh",  "album": "El viaje de Copperpot",   "sold":1100000, "country":"España"},
    {"year":1991, "artist":"Mecano",                "album": "Aidalai",                 "sold":1000000, "country":"España"},
    {"year":1997, "artist":"Luis Miguel",           "album": "Romances",                "sold":800000,  "country":"México"},
    {"year":2000, "artist":"Alejandro Sanz",        "album": "El alma al aire",         "sold":1300000, "country":"España"},
    {"year":2002, "artist":"David Bisbal",          "album": "Corazón latino",          "sold":1300000, "country":"España"},
    {"year":1985, "artist":"Rocío Jurado",          "album": "Paloma Brava",            "sold":700000,  "country":"España"},
    {"year":1997, "artist":"Alejandro Sanz",        "album": "Más",                     "sold":2200000, "country":"España"},
    {"year":1990, "artist":"Julio Iglesias",        "album": "Raíces",                  "sold":1100000, "country":"España"},
    {"year":1996, "artist":"Rosana Lunas",          "album": "Rotas",                   "sold":1100000, "country":"España"},
    {"year":1998, "artist":"Chayanne Atado",        "album": "a tu amor",               "sold":1000000, "country":"Puerto Rico"},
    {"year":1993, "artist":"Abba",                  "album": "ABBA Gold",               "sold":800000,  "country":"Suecia"},
    {"year":2001, "artist":"Álex Ubago",            "album": "¿Qué pides tú?",          "sold":900000,  "country":"España"},
    {"year":1988, "artist":"Mecano",                "album": "Descanso Dominical",      "sold":1100000, "country":"España"},
    {"year":2002, "artist":"Amaral",                "album": "Estrella de mar",         "sold":800000,  "country":"España"},
    {"year":1991, "artist":"Alejandro Sanz",        "album": "Viviendo deprisa",        "sold":800000,  "country":"España"},
    {"year":1995, "artist":"Alejandro Sanz",        "album": "3",                       "sold":800000,  "country":"España"},
    {"year":1997, "artist":"Backstreet Boys",       "album": "Backstreet's Back",       "sold":800000,  "country":"Reino Unido"},
    {"year":1996, "artist":"Ella baila sola",       "album": "Ella baila sola",         "sold":700000,  "country":"España"},
    {"year":1999, "artist":"Estopa",                "album": "Estopa",                  "sold":1100000, "country":"España"},
    {"year":1997, "artist":"Mónica Naranjo",        "album": "Palabra de Mujer",        "sold":1000000, "country":"España"},
    {"year":1981, "artist":"Julio Iglesias",        "album": "De niña a mujer",         "sold":700000,  "country":"España"},
    {"year":1982, "artist":"Michael Jackson",       "album": "Thriller",                "sold":700000,  "country":"Estados Unidos"},
    {"year":1989, "artist":"Phil Collins",          "album": "...But Seriously",        "sold":700000,  "country":"Reino Unido"},
    {"year":1979, "artist":"Rocío Jurado",          "album": "Señora",                  "sold":900000,  "country":"España"},
    {"year":2003, "artist":"Alejandro Sanz",        "album": "No es lo mismo",          "sold":800000,  "country":"España"},
    {"year":2004, "artist":"David Bisbal",          "album": "Bulería",                 "sold":1000000, "country":"España"}
]

# -----------------------------------------------------------------------------------------------------------------

def encontrar_disco_mas_vendido(albums):
    diccionario_mas_vendido={}
    num_ventas_mas_alta=0
    for album in albums:
        if(album['sold']>num_ventas_mas_alta):
            num_ventas_mas_alta=album['sold']
            diccionario_mas_vendido = album
    
    return diccionario_mas_vendido

def encontrar_disco_mas_vendido_UK(albums):
    diccionario_mas_vendido={}
    num_ventas_mas_alta=0
    for album in albums:
        if(album['sold']>num_ventas_mas_alta and album['country']=='Reino Unido'):
            num_ventas_mas_alta=album['sold']
            diccionario_mas_vendido = album

    return diccionario_mas_vendido

def econtrar_disco_estrella_de_mar(albums):
    estrella_de_mar={}
    for album in albums:
        if(album['album']=='Estrella de mar'):
            estrella_de_mar = album

    return estrella_de_mar

def encontrar_disco_mas_vendido_notES(albums):
    diccionario_mas_vendido={}
    num_ventas_mas_alta=0
    for album in albums:
        if(album['sold'] > num_ventas_mas_alta and album['country'] != 'España'):
            num_ventas_mas_alta=album['sold']
            diccionario_mas_vendido = album

    return diccionario_mas_vendido

def encontrar_album_mas_vendido_2da_mitad_90s_ES(albums):
    diccionario_mas_vendido={}
    num_ventas_mas_alta=0
    for album in albums:
        if(album['sold'] > num_ventas_mas_alta and album['country'] == 'España' and 1999 >= album['year'] >= 1995):
            num_ventas_mas_alta=album['sold']
            diccionario_mas_vendido = album

    return diccionario_mas_vendido

def devolver_albumes_mas_vendidos_cada_anio(albums):
    diccionario_devolver={}
    for album in albums:
        year=album['year']
        if year not in diccionario_devolver or album['sold'] > diccionario_devolver[year]['sold']:
            diccionario_devolver[year]=album
    
    return diccionario_devolver
            
# -----------------------------------------------------------------------------------------------------------------

def imprimir_album_mas_vendido(alb):
    print(f"El disco más vendido fue {alb['album']} del artista {alb['artist']} que vendió {alb['sold']} álbumes")

def imprimir_album_mas_vendido_UK(alb):
    print(f"El disco más vendido en Reino Unido fue {alb['album']} en el año {alb['year']}")

def imprimir_estrella_de_mar(alb):
    print(f"El disco Estrella de mar vendió {alb['sold']} álbumes en el año {alb['year']}")

def imprimir_disco_mas_vendido_notES(alb):
    print(f"El disco no español más vendido fue {alb['album']} del artista {alb['artist']}")

def imprimir_disco_mas_vendido_2a_mitad_90s_ES(alb):
    print(f"El álbum en español más vendido en la segunda mitad de la década de los 90 fue {alb['album']} del artista {alb['artist']}")

def imprimir_album_mas_vendido_por_año(alb):
    print(alb)
# -----------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    album = encontrar_disco_mas_vendido(ALBUMES)
    albumUK = encontrar_disco_mas_vendido_UK(ALBUMES)
    estrella = econtrar_disco_estrella_de_mar(ALBUMES)
    albumNotES = encontrar_disco_mas_vendido_notES(ALBUMES)
    albumES2daMitad90s = encontrar_album_mas_vendido_2da_mitad_90s_ES(ALBUMES)
    album_pruebas = devolver_albumes_mas_vendidos_cada_anio(ALBUMES)
    alb = devolver_albumes_mas_vendidos_cada_anio(ALBUMES)
    
    # imprimir_album_mas_vendido(album)
    # imprimir_album_mas_vendido_UK(albumUK)
    # imprimir_estrella_de_mar(estrella)
    # imprimir_disco_mas_vendido_notES(albumNotES)
    # imprimir_disco_mas_vendido_2a_mitad_90s_ES(albumES2daMitad90s)
    imprimir_album_mas_vendido_por_año(alb)
    
    
