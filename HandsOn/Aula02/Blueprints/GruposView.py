#!/usr/bin/python

from flask import Blueprint, jsonify

grupo = Blueprint("grupo", __name__)



@grupo.route("/grupos")
def grupos():
    response = {"message":"Pagina de Grupos"}
    return jsonify(response)

