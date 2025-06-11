import os
from flask import Flask, request, jsonify, render_template
import google.generativeai as genai

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=tmpl_dir)

# Load API key from environment
API_KEY = os.getenv("GOOGLE_GENAI_API_KEY")

if not API_KEY:
    raise ValueError("GOOGLE_GENAI_API_KEY not set in environment")

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    try:
        text = request.json['text']
        response = model.generate_content(text)
        generated_text = response.text
        return jsonify({'generated_text': generated_text})
    except Exception as e:
        print(f"Error during text generation: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
