#!/usr/bin/python

import requests
import json

headers ={ "Content-Type":"application/json"}

novos = [
"Joao Mendes",
"Joaquim Seferino",
"Nicolas Farias",
"Rodrigo Marcelo",
"Maria Joana",
"Abdias Moraes",
"Eliana Sorriso",
"Hellen Gonzaga",
"Humberto Sales",
"Benedito da Silva"
]

for usuario in novos:
    nome = usuario
    
    email = nome.replace(" ",".").lower()+"@dexter.com.br"
    data={"nome":nome, "email":email}
    response = requests.post("http://localhost:5000/usuarios/", 
                             data=json.dumps(data),
                             headers=headers)
    

