from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Load the corpus from the JSON file
with open('corpus.json', 'r', encoding='utf-8') as f:
    corpus = json.load(f)

# Home route
@app.route('/')
def index():
    return render_template('index.html', corpus=corpus)

# Search route
@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q', '').lower()
    filtered_corpus = [word for word in corpus if query in word['sanskrit'].lower() or query in word['malayalam'].lower()]
    return jsonify(filtered_corpus)

if __name__ == '__main__':
    app.run(debug=True)
