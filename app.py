from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
import os
from flask import Flask, request, render_template, g, redirect, Response, send_from_directory

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
print(tmpl_dir)
app = Flask(__name__, template_folder=tmpl_dir)


app = Flask(__name__)
API_KEY = "AIzaSyA4qNAV1x-U9KpGxUMyoPGup9u3ElSyK0A" 
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')
@app.route('/',methods = ['GET'])
def index():
    print(request.args)
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
        return jsonify({'error': str(e)}), 
if __name__ == '__main__':
    app.run(debug=True)