#!/usr/bin/python

#Para testar o mongo:
# $mongo
# use dexter-api   (para abrir o bd)
# show collections  (para monstrar as "tabelas"(collections)
# db.tabela.find()  (para fazer select)
#


from flask import Flask
#import da bibioteca do Mongo
from flask_mongoengine import MongoEngine
from datetime import datetime

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {"db":"dexter-api"}

db = MongoEngine(app)


class Usuarios(db.Document):
    nome = db.StringField()
    email = db.StringField(unique=True) # Para campo Chave - unique=True
    date_cadastro = db.DateTimeField(default=datetime.now())

class Grupos(db.Document):
    nome = db.StringField(unique=True)
    integrantes = db.ListField()



if __name__=="__main__":
#    u = Usuarios()
#    u.nome = "Alex"
#    u.email = "alexandercn@hotmail.com"
#    u.save()

#    g = Grupos()
#    g.nome = "Developers"
#    g.integrantes.append("Alex")
#    g.save()

    todos = Grupos.objects() # Traz todos os objetos (itens) dentro da collection Grupos
    for g in todos:
        print g.nome

    buscado = Grupos.objects(nome="Developers").first()
    print buscado.nome
    print buscado.integrantes

#    buscado.nome = "Comercial"
#    buscado.save()

