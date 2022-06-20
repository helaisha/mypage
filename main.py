from flask import Flask, request , jsonify
import requests
import traceback
import logging

app = Flask(__name__)

@app.route("/home", methods=['GET'])
@app.route("/")
def base():
    return jsonify({"msgcode": 1, "status": "success", "message": "Welcome To My Page"}), 200


@app.route("/admin", methods=['GET'])
def admin():
    try :

        print('This is my first page')



        return jsonify({"msgcode": 1, "status": "success", "message": "Welcome To My Page"}), 200

    except Exception as p :
        return jsonify({"msgcode": 4, "status": "failed", "message": "Failed to Connect  {}".format(p)}), 401





app.run(debug=True)

