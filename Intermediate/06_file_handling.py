### File Handling ###

import os

# .txt file

# Leer, escribir y sobrescribir si ya existe

txt_file = open("Intermediate/my_file.txt", "w+") # Si no está lo crea
txt_file.write(
    "Mi nombre es Gustavo\nMi apellido es Rivera\n29 años\nY mi lenguaje preferido es Python")

# print(txt_file.read())
print(txt_file.read(10)) # Para los 10 primeros caracteres
print(txt_file.readline()) # Lee la primera linea
print(txt_file.readline()) # Lee la segunda
for line in txt_file.readlines(): # Lee lo que queda
    print(line)

txt_file.write("\nAunque también me gusta Kotlin")
print(txt_file.readline())

txt_file.close() # Cerrar cuando acabamos de hacer cosas

with open("Intermediate/my_file.txt", "a") as my_other_file:
    my_other_file.write("\nY Swift")

# os.remove("Intermediate/my_file.txt") Borrar el fichero

# .json file

import json

#Json es como un diccionario, clave-valores.

json_file = open("Intermediate/my_file.json", "w+") # Abrir y si no está, crearlo

json_test = {
    "name": "Gustavo",
    "surname": "Rivera",
    "age": 29,
    "languages": ["Python", "Swift", "Java"]}

json.dump(json_test, json_file, indent = 4)

json_file.close() # Debemos cerrar para leer porque estamos creando

with open("Intermediate/my_file.json") as my_other_file:
    for line in my_other_file.readlines():
        print(line)


json_dict = json.load(open("Intermediate/my_file.json")) # Pasarlo a diccionario
print(json_dict)
print(type(json_dict))
print(json_dict["name"]) # Usar uno de sus propiedades

# .csv file

import csv

csv_file = open("Intermediate/my_file.csv", "w+")

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name", "surname", "age", "language"])
csv_writer.writerow(["Gustavo", "Rivera", 29, "Python"])
csv_writer.writerow(["Roswell", "", 2, "COBOL", ""])

csv_file.close()

with open("Intermediate/my_file.csv") as my_other_file:
    for line in my_other_file.readlines():
        print(line)


# .xlsx file
# import xlrd # Debe instalarse el módulo

# .xml file
import xml