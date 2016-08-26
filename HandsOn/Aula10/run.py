#!/usr/bin/python

from Modulos.Docker import Docker
from flask import Flask, render_template, jsonify, request
# diretorios padrao do render_template:
# - template
# - static
#   |- css    |
#   |- fonts  | Arquivos do bootstrap
#   |- js     |
#
# Baixar arquivos BootStrap
# http://getbootstrap.com/getting-started/#download
#
# Baixar JQuery 
# https://jquery.com/download/
# static - js - jquery.min.js




app = Flask(__name__)

@app.route("/")
def index():

    docker = Docker()
    containers = docker.list_container()
    # **, containers=containers**  Passa uma variavel para o render do index.html - Sera substituido no html
    return render_template("index.html", containers=containers) 



@app.route("/container/stop", methods=["POST"])
def stop():
    cid = request.form["cid"]
    #print cid
    docker = Docker()
    message = docker.stop_container(cid)
    return jsonify(message)
  

@app.route("/container/start", methods=["POST"])
def start():
    cid = request.form["cid"]
    #print cid
    docker = Docker()
    message = docker.start_container(cid)
    return jsonify(message)
  

@app.route("/container/criar", methods=["POST"])
def criar():
    name = request.form["name"]
    image = request.form["image"]    
    docker = Docker()
    message = docker.create_container(name, image)
    return jsonify(message)



if __name__=="__main__":
    app.run(debug=True)
    
    






