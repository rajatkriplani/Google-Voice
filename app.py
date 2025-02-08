import os
import requests
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS  # Only needed if your client and server are on different origins

app = Flask(__name__)
CORS(app)  # Enable CORS if needed (for example, during development)

# Load API key from environment variable
API_KEY = os.environ.get("GEMINI_API_KEY")
if not API_KEY:
    raise RuntimeError("GEMINI_API_KEY environment variable is not set!")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/generate-content', methods=['POST'])
def generate_content():
    # Get JSON payload from the client
    payload = request.get_json()
    if not payload:
        return jsonify({"error": "Invalid JSON payload"}), 400

    # Build the Google API URL with your secure API key
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"
    
    try:
        # Forward the payload to the Google Generative Language API
        response = requests.post(url, json=payload)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Failed to reach external API", "details": str(e)}), 500

    # Return the API response back to the client
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)