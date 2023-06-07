### Regular Expressions ###

# Nos vale para inspeccionar si una cadena de texto tiene cosas o elementos
# Es capaz de dicirnos lo que tiene y retornarnos las ocurrencias de lo que coincide

import re

# match 
# Intenta aplicar un patron. 

my_string = "Esta es la lección número 7: Lección llamada Expresiones Regulares"
my_other_string = "Esta no es la lección número 6: Manejo de ficheros"

match = re.match("Esta es la lección", my_string, re.I) # Propiedad de la biblioteca
                                            # que ignora cosas de como está escrito
print(match)
start, end = match.span()
print(my_string[start:end])

print(re.match("Esta es la lección", my_string))
print(re.match("Esta es la lección", my_other_string))
print(re.match("Expresiones Regulares", my_string))

match = re.match("Esta no es la lección", my_other_string)
# if not(match == None): # Otra forma de comprobar el None
# if match != None: # Otra forma de comprobar el None
if match is not None:
    print(match)
    start, end = match.span()
    print(my_other_string[start:end])

# Esta la empieza a buscar desde el principio

# search
# Entre que punto y que punto encuentra la primera ocurrencia

search = re.search("lección", my_string, re.I)
print(search)
start, end = search.span()
print(my_string[start:end])

# findall
# Listado de las veces que ha encontrado la ocurrencia

findall = re.findall("lección", my_string, re.I)
print(findall)

# split
# Buscar un patrón y divide a partir de allí

print(re.split(":", my_string))

# sub
# Sustituir en la cadena

print(re.sub("[l|L]ección", "LECCIÓN", my_string))
print(re.sub("Expresiones Regulares", "RegEx", my_string))

### Regular Expressions Patterns ###

# Para aprender y validar expresiones regulares: https://regex101.com

pattern = r"[lL]ección"
print(re.findall(pattern, my_string)) # Búsqueda que contenga estos caracteres

pattern = r"[lL]ección|Expresiones"
print(re.findall(pattern, my_string))

pattern = r"[0-9]"
print(re.findall(pattern, my_string))
print(re.search(pattern, my_string))

pattern = r"\d" # No tiene en cuenta los caracteres no numericos y sí los numéricos
print(re.findall(pattern, my_string))

pattern = r"\D"
print(re.findall(pattern, my_string))

pattern = r"[l].*"
print(re.findall(pattern, my_string))

email = "gustavors1@gmail.com"
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-.]+$" # Lógica para buscar emails
print(re.match(pattern, email))
print(re.search(pattern, email))
print(re.findall(pattern, email))

# https://github.com/Asabeneh/30-Days-Of-Python/blob/master/images/regex.png
# Tabla para expresiones regulares