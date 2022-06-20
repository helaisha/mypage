from flask import Flask, request , jsonify
import requests
import traceback
import logging

application = Flask(__name__)

@application.route('/')
def base():
    return 'Welcome To My Page'


@application.route("/admin", methods=['GET'])
def admin():
    try :

        print('This is my first page')



        return jsonify({"msgcode": 1, "status": "success", "message": "Welcome To My Page"}), 200

    except Exception as p :
        return jsonify({"msgcode": 4, "status": "failed", "message": "Failed to Connect  {}".format(p)}), 401







