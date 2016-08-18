#!/usr/bin/python


from flask import Blueprint, jsonify, json, request
from Models.Model import Usuarios as UsuariosModel


usuario = Blueprint("usuario", __name__)


@usuario.route("/usuarios/", methods=["GET"])
def usuarios():
    todos = json.loads(UsuariosModel.objects().to_json())
    response = {"usuarios":todos}
    return jsonify(response)


@usuario.route("/usuarios/", methods=["POST"])
def add_usuarios():
    print request.get_json()
    response = {"message":"Cadastro de Usuarios"}
    return jsonify(response)





@usuario.route("/usuarios/<id>", methods=["PUT"])
def update_usuarios(id):
    response = {"message":"Atualizacao de Usuario"}
    return jsonify(response)


@usuario.route("/usuarios/<id>", methods=["DELETE"])
def delete_usuarios(id):
    response = {"message":"Excluir Usuario %s"%id }
    return jsonify(response)

@usuario.route("/usuarios/<id>/", methods=["GET"])
def get_usuarios(id):
    status_cod = 200 #para retornar status da  pagina, por exemplo 404 Page not Found
    response = {"message":"Mostando Usuario %s"%id}
    return jsonify(response), status_cod


