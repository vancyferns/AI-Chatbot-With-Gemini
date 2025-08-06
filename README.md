# AI-Chatbot-With-Gemini

<body style="font-family: Arial, sans-serif; line-height: 1.6; padding: 20px; background: #f9f9f9; color: #333;">

  <h1>🚀 Gemini Chatbot (React + Flask + Gemini API)</h1>

  <p>This is a full-stack chatbot app powered by Google Gemini's generative AI. The frontend is built with React, and the backend is a Flask server using the Gemini 2.5 Flash model.</p>

  <h2>🧱 Tech Stack</h2>
  <ul>
    <li><strong>Frontend:</strong> React, Vite, CSS</li>
    <li><strong>Backend:</strong> Python Flask</li>
    <li><strong>AI API:</strong> Google Gemini (Generative AI)</li>
  </ul>

  <h2>📦 Installation</h2>

  <h3>1. Backend Setup</h3>
  <pre><code>
git clone https://github.com/your-username/gemini-chat-app.git
cd backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
  </code></pre>

  <p>Create a <code>.env</code> file in the backend directory and add:</p>
  <pre><code>GEMINI_API_KEY=your_google_gemini_api_key</code></pre>

  <p>Then start the Flask server:</p>
  <pre><code>python app.py</code></pre>

  <h3>2. Frontend Setup</h3>
  <pre><code>
cd frontend
npm install
npm run dev
  </code></pre>

  <h2>🔁 API Endpoint</h2>
  <ul>
    <li><code>POST /chat</code> - Accepts JSON with a "message" key and returns the Gemini AI response.</li>
  </ul>

  <h2>📄 Example Request</h2>
  <pre><code>
POST /chat
Content-Type: application/json

{
  "message": "Tell me a joke."
}
  </code></pre>

  <h2>💬 Output</h2>
  <pre><code>
{
  "response": "Why did the scarecrow win an award? Because he was outstanding in his field!"
}
  </code></pre>

  <h2>🎨 Styling</h2>
  <p>The UI is clean and minimal, styled using <code>index.css</code> and <code>App.css</code>.</p>

  <h2>🛡️ CORS</h2>
  <p>Flask uses <code>flask-cors</code> to allow frontend access. Adjust origins in production.</p>



</body>

