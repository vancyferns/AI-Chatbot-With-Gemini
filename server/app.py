from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv
import google.generativeai as genai
from flask_cors import CORS


# Load environment variables
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize Flask
app = Flask(__name__)
CORS(app)  # Allow all origins; for production, use CORS(app, origins=['https://your-frontend.com'])

# Create chat model
model = genai.GenerativeModel('gemini-2.5-flash')
chat = model.start_chat()

# Test route
@app.route('/', methods=['GET'])
def home():
    return "✅ Gemini Chat API is running!", 200

# Chat route
@app.route('/chat', methods=['POST'])
def chat_route():
    if not request.is_json:
        return jsonify({"error": "Invalid content type, must be application/json"}), 400

    data = request.get_json()
    user_input = data.get("message", "")

    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    try:
        response = chat.send_message(user_input)
        return jsonify({"response": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the app on 0.0.0.0 to allow external access
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
