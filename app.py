from flask import Flask, render_template, request, jsonify
from transformers import pipeline

app = Flask(__name__)

try:
    # Load the translation pipeline
    translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-fi")

except Exception as e:
    print("Error loading model", e)

@app.route('/')
def index():
    # Serve the HTML template
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():

    # Get text from the form
    input_text = request.form.get('text')
    if not input_text:
        return jsonify({"error": "No text provided"}), 400

    # Translate the text using the pipeline
    translated = translator(input_text, max_length=400)
    translated_text = translated[0]['translation_text']

    # Return the translated text as JSON
    return jsonify({"translated_text": translated_text})

if __name__ == "__main__":
    app.run(debug=True)
