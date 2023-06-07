### Users API ###

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

# Iniciamos con uvicorn Backend.FastAPI.users:app --reload

# Entidad user

class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: str

users_list = [User(id=1, name="Gustavo", surname="Rivera", url="https://rivera.dev", age=29),
              User(id=2, name="Andres", surname="Martin",
                   url="https://martindev.com", age=35),
              User(id=3, name="Luis", surname="Dahlberg", url="https://ldahlberg.com", age=33)]

@router.get("/usersjson")
async def usersjson():  # Creamos un JSON a mano
    return [{"name": "Gustavo", "surname": "Rivera", "url": "https://rivera.dev", "age": 29},
            {"name": "Andres", "surname": "Martin",
                "url": "https://martindev.com", "age": 35},
            {"name": "Luis", "surname": "Dahlberg", "url": "https://ldahlberg.com", "age": 33}]

@router.get("/users")
async def users():
    return users_list

"""
El parámetro Path se utiliza para capturar valores específicos dentro de la ruta de la URL. 
Puedes definir el parámetro Path en tu función de manejo de ruta como argumento, 
y FastAPI lo capturará automáticamente para ti.
"""

@router.get("/user/{id}")  # Path 
async def user(id: int):
    return search_user(id)

"""
El parámetro Query se utiliza para capturar los valores proporcionados en la URL 
como parámetros de consulta (query parameters). 
Los parámetros de consulta se agregan a la URL 
después del símbolo de interrogación (?) 
y se utilizan para proporcionar datos adicionales a la solicitud.
"""

@router.get("/user/")  # Query, igualar una clave a un valor.
async def user(id: int):
     return search_user(id)
    
"""
Path se utiliza para capturar valores específicos dentro de la ruta de la URL, 
mientras que Query se utiliza para capturar los parámetros de consulta 
proporcionados en la URL después del símbolo de interrogación.
"""

# Utilización de Post
# Response model para la documentación

@router.post("/user/", response_model=User, status_code=201) # Por defecto, el código de status quiero con esto
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=404, detail ="El usuario ya existe")
    # raise propaga la excepción
        # return {"error" : "El usuario ya existe"} Cambiamos para HTTPexception
    else:
        users_list.append(user)
        return user

# Utilización de Put

#Actualizar el usuario

@router.put("/user/")
async def user(user: User):

    found = False

    for index, saved_user in enumerate(users_list): # Para recorrer la lista
        if saved_user.id == user.id: # Si encontramos al usario
            users_list[index] = user # Con este le decimos que lo actualice
            found = True

    if not found:
        return {"error": "No se ha actualizado el usario"}
    else:
        return user # Si de verdad lo hemos actualizado retorna un usuario. 
    
# Delete

@router.delete("/user/{id}")
async def user(id: int):

    found = False

    for index, saved_user in enumerate(users_list): 
        if saved_user.id == id:
            del users_list[index]
            found = True

    if not found:
        return {"error": "No se ha eliminado el usario"}
    
def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "no se ha encontrado el usaurio"}