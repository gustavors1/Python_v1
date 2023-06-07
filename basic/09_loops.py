### Loops (bucles, ciclos) ###

# Nos sirve para iterar, que es repetir algo
# Pasamos por el código varias veces

# While

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2 # Autoincrimentando de a 1, y así frena el bucle
else: # Es opcional
    print("Mi condición es mayor o igual que 10")

print("La ejecución continua")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Se detiene la ejecución")
        break
    print(my_condition)
    
print("La ejecución continua")

# For

# Nos sirve para iterar un listado de elementos

my_list = [35, 24, 62, 30, 30, 17]

for element in my_list: # Ha impreso cada elemento
    print(element)

my_tuple = (29, 1.62, "Gustavo", "Rivera", "Rivera")
for element in my_tuple:
    print(element)

my_set = {"Gustavo", "Rivera", 29}
for element in my_set:
    print(element)

my_dict = {
    "Nombre": "Gustavo", 
    "Apellido": "Rivera", 
    "Edad" :29, 
    "Lenguajes": {"Python", "Swift", "Kotlin"},
    1:1.77
    }
for element in my_dict:
    print(element)
    if element == "Edad":
        break
else:
    print("El cuble for para diccionario ha finalizado")

for element in my_dict:
    print(element)
    if element == "Edad":
        continue # No se recomienda usar mucho como en lenguajes actuales.
                # Vuelve al for sin ejecutar lo que está debajo
else:
    print("Se ejecuta")

print("La ejecución continua")