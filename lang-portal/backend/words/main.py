from flask import Blueprint, jsonify
from .entity import WordsNQ

words = Blueprint('words', __name__)

@words.route('/words')
def index():
    return jsonify(WordsNQ.allwords())

@words.route('/words/<int:word_id>')
def show_post(word_id):
        response={}
        response["response"]=WordsNQ.getWord(word_id)
        return jsonify(response)