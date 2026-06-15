from flask import Flask, request, jsonify
import os
from google import genai

app = Flask(__name__)

client = genai.Client(api_key=os.environ.get('GEMINI_API_KEY'))

@app.route('/')
def index():
    return 'OK'

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    message = data.get('message', '')
    response = client.models.generate_content(
        model='gemini-2.0-flash',
        contents=message
    )
    return jsonify({'reply': response.text})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
