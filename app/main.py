import os
import openai

# import translators
import translators

# Flask API interface
from flask import Flask, request, jsonify
app = Flask(__name__)

## application/x-www-form-urlencoded
@app.route('/natToCypher', methods=['POST'])
def natToCypher():
    data = request.form
    natural_language = data['natural_language']
    cypher_query = translators.generate_cypher(natural_language)
    return jsonify({
        'natural_language': natural_language,
        'cypher_query': cypher_query
        }
    )

if __name__ == '__main__':
    app.run(debug=True, port=8080)