### Dictionaries ###

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

# Relación clave- valor
my_other_dict = {"Nombre": "Gustavo", "Apellido": "Rivera", "Edad" :29, 1:"Python"}

my_dict = {
    "Nombre": "Gustavo", 
    "Apellido": "Rivera", 
    "Edad" :29, 
    "Lenguajes": {"Python", "Swift", "Kotlin"},
    1:1.77
    }

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

print(my_dict["Nombre"])

my_dict["Nombre"] = "Pedro" # Actualizando Clave
print(my_dict["Nombre"])

print(my_dict[1])

my_dict["Calle"] = "Calle Rivera" # Agregar un nuevo campo
print(my_dict)

del my_dict["Calle"] # Eliminar un solo elemento
print(my_dict)

print("Rivera" in my_dict)
print("Apellido" in my_dict) # Se busca por clave
print(my_dict ["Apellido"]) # Buscar dentro de una clave

print(my_dict.items()) # Listado de cada una de las items (clave + valor)
print(my_dict.keys()) # Listado de claves
print(my_dict.values()) # Listado de los valores de las claves

my_list = ["Nombre", 1, "Piso"] # Nuevo diccionario

my_new_dict = dict.fromkeys((my_list))
print(my_new_dict) 
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict) # Me creo un nuevo diccionario con las claves
                                    # de my_dict
print(my_new_dict)