from pymongo import MongoClient

# Base de datos remota con Mongo Atlas

db_client = MongoClient("mongodb+srv://test:test@cluster0.ia5phdr.mongodb.net/?retryWrites=true&w=majority").test

