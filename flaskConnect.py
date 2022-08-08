from flask import Flask, jsonify, request

from Chatbot import *

app = Flask(__name__)

@app.route('/get/message', methods=['POST'])
def food():
    req = request.json
    result = getMessage(req['message'])
    return jsonify(result)

@app.route('/', methods=['GET'])
def get():
    return jsonify({"Done" : True})
