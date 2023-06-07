### Exceptions Handling ###

numberOne = 5 
numberTwo = 1 
numberTwo = "1"

# Excepción base: try except

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    # Se ejecuta si se produce una excepcion
    print("Se ha producido un error")

# Flujo completo de una excepción: try except else finally

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else: 
    # Se ejecuta si no se produce una excepción
    print("La ejecución continua correctamente")
finally:
    # Se ejecuta siempre, con error o no
    print("La ejecución continua")

# Excptions por tipo
try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except TypeError:
    # Se ejecuta si se produce una excepcion
    print("Se ha producido un TypeError")
except ValueError:
    print("Se ha producido un ValueError")

# Captura de la información de la excepción

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError as error: # Nombre de la variable que contiene el error 
    print(error)
except Exception as my_random_error_name:# Sea lo que sea el error 
                                        # y no es el anterior se imprime esto
    print(my_random_error_name)