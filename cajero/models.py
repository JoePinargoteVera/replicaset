from datetime import datetime
from flask_mongoengine import MongoEngine

db = MongoEngine()

# Definición del modelo para la colección "Cliente"
class Cliente(db.Document):
    nombre = db.StringField(required=True)
    cedula = db.StringField(required=True, unique=True)
    clave = db.IntField(required=True)
    saldo = db.FloatField(required=True)
    meta = {
        'collection': 'cliente'
    }

# Definición del modelo para la colección "Ingreso"
class Ingreso(db.Document):
    cliente = db.ReferenceField(Cliente, required=True)
    monto = db.FloatField(required=True)
    fecha = db.DateTimeField(required=True, default=datetime.utcnow)
    meta = {
        'collection': 'ingreso'
    }

# Definición del modelo para la colección "Egreso"
class Egreso(db.Document):
    cliente = db.ReferenceField(Cliente, required=True)
    monto = db.FloatField(required=True)
    fecha = db.DateTimeField(required=True, default=datetime.utcnow)
    meta = {
        'collection': 'egreso'
    }
