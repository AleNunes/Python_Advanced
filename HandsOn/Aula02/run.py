#!/usr/bin/python

from flask import Flask, jsonify
from Blueprints.UsuariosView import usuario
from Blueprints.GruposView import grupo

#Instaciando aplicacao flask
app = Flask(__name__)
#registrando as  blueprints
app.register_blueprint(usuario)
app.register_blueprint(grupo)


#criando rota para index
@app.route("/")
def index():
    response = {"message":"Pagina Index"}
    return jsonify(response)




if __name__=="__main__":
    #app.run(host="0.0.0.0", port=5001)
    app.run(host="0.0.0.0", port=5001, debug=True) #debug=True roda novamente aplicacao quando o arquivo eh salvo











