# Las listas son mutables, se declaran delimitando los elementos que forman la coleccion entre corchetes. Tabien se accede a los elementos empleando los corchetes y la posición

lenguajes = ['Java','SQL', 'Python', 'HTML', 'XML', 'CSS', 'PHP']

print(f'Vamos a aprender sobre el lenguaje de programación de {lenguajes[2]}')

# Añadir nuevos lenguajes
lenguajes.append('JavaScript')
print(lenguajes)