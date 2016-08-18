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
    data = request.get_json()
    novo = UsuariosModel()

    #novo.nome = data.get("nome")
    #novo.email = data.get("email")
    for k in data.keys():
        setattr(novo, k , data.get(k))

    novo.save()
    response = {"message":"Usuarios cadastrado"}
    return jsonify(response)





@usuario.route("/usuarios/<id>", methods=["PUT"])
def update_usuarios(id):

    data = request.get_json()
    u = UsuariosModel.objects(id=id).first()

    for k in data.keys():
        setattr(u, k , data.get(k))
    u.save()

    response = {"Usuarios":data}
    return jsonify(response)



@usuario.route("/usuarios/<id>", methods=["DELETE"])
def delete_usuarios(id):

    u = UsuariosModel.objects(id=id).first()
    if not u: #Caso u nao seja encontrado   
        return jsonify({"Message":"Usuario nao encontrado"}),404    #retorna page not found
    #apaga elemento
    u.delete()
    
    response = {"Message":"Usuario excluido"}
    return jsonify(response)




@usuario.route("/usuarios/<id>/", methods=["GET"])
def get_usuarios(id):
    u = UsuariosModel.objects(id=id).first()
    if not u:
        return "Nao encontrado", 404
    u = json.loads(u.to_json())

    status_cod = 200 #para retornar status da  pagina, por exemplo 404 Page not Found
    return jsonify(u), status_cod


