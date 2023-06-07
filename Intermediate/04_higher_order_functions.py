### Higher Order Functions ###

# Son funciones que hacen cosas con funciones adentro, o que ejecutan a otras

from functools import reduce

def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

def sum_two_values_and_value(first_value, second_value, f_sum):
    return f_sum(first_value + second_value)

print(sum_two_values_and_value(5, 2, sum_one))
print(sum_two_values_and_value(5, 2, sum_five))

### Closures ###

def sum_ten(original_value):
    def add(value):
        return value + 10 + original_value
    return add


add_closure = sum_ten(1)
print(add_closure(5))

print((sum_ten(5))(1)) # En una sola forma

### Built-in Higher Order Functions ### 

# Map 
# Recorre todos los valores y ejecuta una función para modificarlos
numbers = [2, 5, 10, 21, 3, 30]

def multiply_two(number):
    return number * 2

print(list(map(multiply_two, numbers))) 

# con un listado iterable 
# genera otro itereble
# en función a la función que nosotros le hemos pasado. 

print(list(map(lambda number: number * 2, numbers))) # Con lambda

# Filter

#  Recorre todos los valores y ejecuta una función que retorna true o false 
# para saber como filtar los valores

def filter_greater_that_ten(number):
    if number > 10:
        return True
    return False

""" 
Manera sencilla:

def filter_greater_that_ten(number):
    return number > 10

"""
print(list(filter(filter_greater_that_ten, numbers)))
print(list(filter(lambda number: number > 10, numbers))) #Con lambda 
# sin crear función

# Reduce

# Operar entre los valores que va a recorrer
# Opera con un valor más el acumulado
# Hay que importarla

def sum_two_values(first_value, secod_value):
    print(first_value)
    print(secod_value)
    
    return first_value + secod_value

print(reduce(sum_two_values, numbers))