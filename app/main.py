import os
import openai

# import translators
import translators

# Flask API interface
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/natToCypher', method=['POST'])
def natToCypher():
    data = request.get_json()
    natural_language = data['natural_language']
    cypher_query = translators.Neo4J(natural_language)
    return jsonify({
        'natural_language': natural_language,
        'cypher_query': cypher_query
        }
    )