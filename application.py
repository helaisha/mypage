from flask import Flask, request , jsonify
import requests
import traceback
import logging

appplication = Flask(__name__)

@appplication.route("/home", methods=['GET'])
@appplication.route("/")
def base():
    return jsonify({"msgcode": 1, "status": "success", "message": "Welcome To My Page"}), 200


@appplication.route("/admin", methods=['GET'])
def admin():
    try :

        print('This is my first page')



        return jsonify({"msgcode": 1, "status": "success", "message": "Welcome To My Page"}), 200

    except Exception as p :
        return jsonify({"msgcode": 4, "status": "failed", "message": "Failed to Connect  {}".format(p)}), 401





appplication.run(debug=True)

