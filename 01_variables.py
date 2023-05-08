# Variables
my_string_variable = "My String variable"
print(my_string_variable)

my_int_variable = 5
print(my_string_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

# Concatenación de variables en un print
print(my_string_variable, my_int_variable, my_bool_variable)
print("Este es el valor de:", my_bool_variable)

# Funciones de sistema
#len cuenta cuantos caracteres hay
print(len(my_string_variable))

# Variables en una sola línea. ¡Cuidado con abusar de esta sintaxis!
name, surname, alias, age = "Gustavo", "Rivera", "Gutavors", "35"
print("Soy:", surname, name, age, alias)

#imputs para pedir información por consola
"""
name = input("¿Cuál es tu nombre? ")
age = input("¿Cuál es tu edad? ")

print(name, "es tu nombre ")
print(age, "años es tu edad ")
"""

# Cambiamos su tipo
name = 35
age = "Gustavo"
print(name)
print(age)
