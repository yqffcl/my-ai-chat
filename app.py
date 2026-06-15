from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    return 'OK'

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    message = data.get('message', '')
    return jsonify({'reply': f'收到：{message}'})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

