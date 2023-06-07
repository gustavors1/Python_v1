### Tuples ###

### a diferencia de las listas en las tuplas son inmutables, lo que he
# decidido no se mueve. 

my_tuple = tuple() # Conjunto de valores
my_other_tuple = ()

my_tuple = (29, 1.62, "Gustavo", "Rivera", "Rivera")
my_other_tuple = (35, 60, 30)

print(my_other_tuple)
print(my_tuple)
print(type(my_tuple))

print(my_tuple[-1])
print(my_tuple[0])
#print(my_tuple[4]) IndexError
#print(my_tuple[-6]) IndexError

print(my_tuple.count("Rivera")) #Contar cuantos valores hay con nombre
print(my_tuple.index("Gustavo")) # En que posición está
print(my_tuple.index("Rivera"))

# my_tuple[1] = 1.80  inmutable

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple) 

print(my_sum_tuple[3:6]) # Buscar elemento

my_tuple = list(my_tuple) # Cambiamos la Tupla a lista
print(type(my_tuple)) 

my_tuple[4] = "rivera"
my_tuple.insert(1, "Azul")
print(my_tuple) # cambiando los valores de la lista

my_tuple = tuple(my_tuple) # Cambiando otra vez a Tupla
print(type(my_tuple))

del my_tuple #la borramos
#print(my_tuple) NameError: name 'my_tuple' is not defined
