### Listas ###

my_list = list()
my_other_list = [] 

# Estos son los dos contrusctores para hacerlo

print(len(my_list))

my_list = [35, 24, 62, 30, 30, 17] # Listas con corchetes

print(my_list)
print(len(my_list))

my_other_list = [35, 1.72, "Gustavo", "Rivera"]

print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])
print(my_list.count(30)) # Para ver cuantas veces repite un elemento en la lista
# print(my_other_list[4]) IndexError
# print(my_other_list[-5]) IndexError

age, height, name, surname = my_other_list
print(name)

print(my_list + my_other_list)
#print(my_list - my_other_list)

my_other_list.append("Mouredv")
print(my_other_list)

my_other_list.insert(1, "Azul")
print(my_other_list)

my_other_list.remove("Azul")
print(my_other_list)

my_list.remove(30) #Solo remueve uno de los 30
print(my_list)

my_other_list[1] = "Rojo" # Modifico el valor
print(my_other_list)

my_list.pop() # Elimina el último elemento
print(my_list)

my_pop_element = my_list.pop(2) # Lo que quiero eliminar lo pongo en variable
print(my_pop_element)
print(my_list)

del my_list[2] # Quitar un dato posicionado de mi lista. Elimina por indice.
print(my_list)

my_new_list = my_list.copy() #Copio antes de eleminarlo por si
                            #  la quiero en otro lado

my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.reverse() # Voltear la lista
print(my_new_list) 

my_new_list.sort() #Por defecto lo ordena de menor a menor o alfabéticamente
print(my_new_list)

print(my_new_list[1:2]) # Ver como índices

my_list = "Hola Python" #Por su tipado dinámico cambio a String
print(my_list)
print(type(my_list))

