### Sets ###
# De base tiene un Array (en Python son listas).

my_set = set() #Palabra reservada para crear el set
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # Inicialmente nos dice que es un diccionario

my_other_set = {"Gustavo", "Rivera", 29}
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add("Gustavoriv")

print(my_other_set) # Un set no es una estructura ordenada. 
                    # No podemos acceder a elemento 0 o 1, olvidarse de listados.

my_other_set.add("Gustavoriv") # Un set no admite repetidos

print(my_other_set)

print("Gustavo" in my_other_set) # Verificar datos con boolean
print("Gustavi" in my_other_set)

my_other_set.remove("Gustavo") # Eliminar elementos
print(my_other_set)

my_other_set.clear() # Borrar todos los elementos
print(len(my_other_set))

del my_other_set
#print(my_other_set) # NameError: name 'my_other_set' is not defined
                    # Borramos como tal la variable

my_set = {"Gustavo", "Rivera", 29}
my_list = list(my_set)
print(my_list) # Lo hemos convertido en una lista
print(my_list[0]) # No se recominda porque igual cambian el orden

my_other_set = {"Python", "Java", "Swift"}

my_new_set = my_set.union(my_other_set)
print(my_new_set)

print(my_new_set.union(my_new_set)) # No acepta repetidos

print(my_new_set.union(my_set).union({"JavaScrpt", "C#"})) # ignora el repetido 
                                                            # y suma el nuevo

print(my_new_set.difference(my_set)) #Le quitamos los de my_set