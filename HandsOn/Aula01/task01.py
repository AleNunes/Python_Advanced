#!/usr/bin/python

import requests
import json

novo={"nome":"Rafael Medeiros", "email":"rafael.medeiros@dexter.com.br"}
cabecalho ={ "Content-Type":"application/json"}




todos = json.loads(requests.get("http://127.0.0.1:5000/usuarios/")._content)


lista = [usuario for usuario in todos.get("usuarios") if usuario.get("email") == novo.get("email")]
print lista
if lista:
    print "Usuario ja cadastrado"         
    response = requests.delete("http://localhost:5000/usuarios/%s/"%(lista[0].get("id")))
    print response._content
response = requests.post("http://localhost:5000/usuarios/", data=json.dumps(novo), headers=cabecalho)
print response._content


'''

usuarios = todos.get("usuarios")
for user in usuarios:
    if user.get("email") ==  novo.get("email"):
        print "Deleter ", user.get("nome")        
        response = requests.delete("http://localhost:5000/usuarios/%s/"%(user.get("id")))
        print response._content
response = requests.post("http://localhost:5000/usuarios/", data=json.dumps(novo), headers=cabecalho)
print response._content

'''
