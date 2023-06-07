### Modules ###

# Lugar donde tenemos código, y queremos acceder a él desde otro fichero.
# Evita la replicación de código.

import basic.my_module as my_module

my_module.sumValue(5, 3, 1)
my_module.printValue("Hola Python")

from basic.my_module import sumValue, printValue

sumValue(5, 3, 1)
printValue("Hola Python")

import math # Modulo del sitema Python

print(math.pi)
print(math.pow(2, 8))

from math import pi as PI_Value
print(PI_Value)
