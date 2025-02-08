# app.py
import os
import requests
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Load your API key from an environment variable (or another secure method)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_ENDPOINT = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/generate", methods=["POST"])
def generate():
    # Get the user input from the POST body
    data = request.get_json()
    # Use a default prompt if none provided
    user_text = data.get("text", "Explain how AI works")
    
    # Prepare the payload for the Gemini API
    payload = {
        "contents": [{
            "parts": [{"text": user_text}]
        }]
    }

    try:
        # Send the POST request to the Gemini API (API key is appended as a query parameter)
        response = requests.post(GEMINI_ENDPOINT, params={"key": GEMINI_API_KEY}, json=payload)
        response.raise_for_status()
        result = response.json()
        return jsonify(result)
    except requests.exceptions.RequestException as e:
        # Log or handle errors as needed
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # Set debug=False in production!
    app.run(debug=True)