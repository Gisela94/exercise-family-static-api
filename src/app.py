"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

#Agregamos a los miembros de la familia
John = {
    "first_name": "John",
    "last_name": jackson_family.last_name,
    "age": 33,
    "lucky_numbers": [7, 13, 22]
}

Jane = {
    "first_name": "Jane",
    "last_name": jackson_family.last_name,
    "age": 35,
    "lucky_numbers": [10, 14, 3]
}

Jimmy = {
    "first_name": "Jimmy",
    "last_name": jackson_family.last_name,
    "age": 5,
    "lucky_numbers": 1
}

#Llamamos a la función add_member y agregamos cada integrante de la familia previamente declarada
jackson_family.add_member(John)
jackson_family.add_member(Jane)
jackson_family.add_member(Jimmy)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def get_members():

    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    response_body = {
        "family": members
    }

    return jsonify(response_body), 200

@app.route('/addmember', methods=['POST'])
def add_member():
    request_body = request.json
    jackson_family.add_member(request_body)
    return jsonify({"Mensaje": "Integrante agregado exitosamente"}), 201

@app.route('/members/<int:id>', methods=['GET'])
def get_member(id):
    request_body = request.json
    jackson_family.get_member(request_body)
    return jsonify({})


@app.route('/members', methods=['DELETE'])
def delete_member(id):
    request_body = request.json
    jackson_family.delete_member(request_body)
    return jsonify({"Mensaje": "Integrante eliminado exitosamente"}), 201

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
