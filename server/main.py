from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app,origins='*')


@app.route('/hello_world')
def hello_world():
    return jsonify({'message': 'Hello, World!'})

if __name__ == '__main__':
    app.run(debug=True, port=8080)