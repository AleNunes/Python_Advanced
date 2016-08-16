#!/usr/bin/python

import requests

response = requests.get("http://127.0.0.1:5000/usuarios/")
#print response.__dict__  #__dict__ traz  todos os valores e atributos do objeto
#print response._content  #_content traz o conteudo do objeto
print response._content, response.status_code  #_content traz o conteudo do objeto


response = requests.get("http://127.0.0.1:5000/usuarios/6/")
print response._content, response.status_code 

import json

###################################################
cabecalho ={ "Content-Type":"application/json"}
###################################################
#Inclusao
#novo={"nome":"Goku", "email":"sayajin@dexter.com.br"}
#response = requests.post("http://localhost:5000/usuarios/", data=json.dumps(novo), headers=cabecalho)
#print response._content

#Update
#novo={"nome":"Rocky Man", "email":"rocky@dexter.com.br"}
#response = requests.put("http://localhost:5000/usuarios/6/", data=json.dumps(novo), headers=cabecalho)
#print response._content

#Delete
response = requests.delete("http://localhost:5000/usuarios/3/")
print response._content

