### Classes ###

# Definición
# Las clases comienzan en mayúscula, sin espacios, sin guiones

class MyEmptyPerson: 
    pass  # Para poder dejar la clase vacía

print(MyEmptyPerson)
print(MyEmptyPerson())

# Clase con constructor, funciones y popiedades privadas y públicas

# class Person:
#    def __init__(self, name, surname):
#        self.name = name
#       self.surname = surname

# my_person = Person("Gustavo", "Rivera")
# print(f"{my_person.name} {my_person.surname}")

class Person:
    def __init__(self, name, surname, alias = "Sin Alias"):
        self.full_name = f"{name} {surname} ({alias})" # Pública
        self.__name = name #Ponerla privada
       

    def get_name (self): #Esto para accede a la privada
        return self.__name
    
    def walk (self):
        print(f"{self.full_name} Está caminando")

my_person = Person("Gustavo", "Rivera")
print(my_person.full_name)
print(my_person.get_name()) # Acceder al privado para lectura
my_person.walk()

my_other_person = Person("Gustavo", "Rivera", "Gustavoriv")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Héctor de León (El loco de los perros)" # Cambio el valor
print(my_other_person.full_name)

my_other_person.full_name = 6666 # Vuelvo a cambiar el valor
print(my_other_person.full_name)