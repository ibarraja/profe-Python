# Almacena la siguiente información sobre los álbumes más vendidos en los años 90 en una lista de diccionarios (menos mal que no existía el Reggaeton):
# Recuerda que cada álbum es un diccionario
# (Artista o grupo, álbum, unidades vendidas y país del artista)
albumes= [
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
    {"year":2002, "artist":"Amaral Estrella",       "album": "de mar",                  "sold":800000,  "country":"España"},
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
# Muestra por consola:
#   - El disco más vendido fue XXX del artista YYY que vendió ZZZ álbumes
#   - El disco más vendido en Reino Unido fue XXX en el año YYY
#   - El disco Estrella de mar vendió XXX álbumes en el año YYY
#   - El disco no español más vendido fue XXX del artista YYY
#   - El álbum en español más vendido en la segunda mitad de la década de los 90 fue XXX del artista YYY
#   - Los álbumes más vendidos cada año de la década fueron:
