from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from meta_ai_api import MetaAI
# import os

app = Flask(__name__, static_folder='')
CORS(app)  # Enable CORS for all routes

ai = MetaAI()

@app.route('/')
def index():
    return send_from_directory('', 'index.html')

@app.route('/api/prompt', methods=['POST'])
def prompt():
    data = request.json
    message = data.get('message', '')
    response = ai.prompt(message=message)
    return jsonify(response)  # Ensure the response is in JSON format

if __name__ == '__main__':
    app.run(debug=True)
