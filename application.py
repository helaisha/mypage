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




if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production application.
    application.debug = True
    application.run(host="0.0.0.0")


