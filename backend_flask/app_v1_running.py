# app.py

# System imports
from flask import Flask, request, jsonify
from flask_cors import CORS
#import sqlite3

# Local imports
#import test_questions as questions
import loi_questions as questions

app = Flask(__name__)
CORS(app)

current_question_index = 0

@app.route('/api/question')
def get_question():
    global current_question_index
    print(f'getting question ndx {current_question_index}')
    question = questions.questions[current_question_index]
    return jsonify({'question': question})

@app.route('/api/org_questions')
def get_org_questions():
    print(f'getting org questions')
    return jsonify({'questions': questions.org_questions})

@app.route('/api/foundation_questions')
def get_foundation_questions():
    print(f'getting foundation questions')
    return jsonify({'questions': questions.foundation_questions})

@app.route('/api/project_questions')
def get_project_questions():
    print(f'getting project questions')
    return jsonify({'questions': questions.foundation_questions})

@app.route('/api/submit_answer', methods=['POST'])
def submit_answer():
    global current_question_index
    print('answer submitted')
    data = request.get_json()
    print(data)
    answer = data['answer']

    # Save answer to database here
    # for testing
    print(f'saving answer to database: {answer}\n current question index: {current_question_index}')
    # Connect to SQLite database to store data (makes it accessible to front-end)
    #conn = sqlite3.connect('questions.db')
    #c = conn.cursor()

    #return get_question()
    return jsonify({'success': True})

if __name__ == '__main__':
    print('starting up app')
    app.run(debug=False)
