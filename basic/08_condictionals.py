### Conditionals ###

# La manera de establecer flujos de ejecución en nuestro código

my_condition = False

if my_condition: # Al escribir esto se supone que debe ser verdadero
                # Es lo mismo que if my_condition == True
    print("Se ejecuta la condición del if")

my_condition = 5 * 5 

if my_condition == 10:
    print("Se ejecuta la condición del segundo if")

# if, elif, else

if my_condition == 10:
    print("Se ejecuta la condición del tercer if")

if my_condition > 10:
    print("Es mayor que 10")
else: # Si no se cumple el if, se cumple el else
    print("Es menor o igual a 10") 

if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menor que 20")
elif my_condition == 25:
    print("Es igual a 25") 
else: # Si no se cumple el if, se cumple el else
    print("Es menor o igual a 10 o mayor o igual que 20") 

print("La ejecución continúa")

# Condicional con ispección de valor

my_string = ""

if not my_string:
    print("Mi cadena de texto es vacía")

if my_string == "Mi cadena de textooo":
    print("Estas cadenas de texto coinciden")
