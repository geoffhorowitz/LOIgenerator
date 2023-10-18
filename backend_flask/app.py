# app.py

# System imports
from flask import Flask, request, jsonify
from flask_cors import CORS
#import sqlite3

# Local imports
import loi_questions as questions

app = Flask(__name__)
CORS(app)

@app.route('/api/num_questions', methods=['GET', 'POST'])
def get_num_questions():
    print(f'getting the number of questions')
    data = request.get_json()
    #print(data)
    list_id = data['endpoint']
    if list_id == 'org_questions': res = len(questions.org_questions)
    elif list_id == 'foundation_questions': res = len(questions.foundation_questions)
    elif list_id == 'project_questions': res = len(questions.project_questions)
    else: res = 0
    return jsonify({'n_questions': res})

@app.route('/api/org_questions', methods=['POST'])
def get_org_questions():
    print(f'getting org questions')
    print(request.data)
    data = request.get_json()
    print(data)
    ndx = data['question_ndx'] if data and ('question_ndx' in data) else 0
    print('responding with ', questions.org_questions[ndx])
    return jsonify({'question': questions.org_questions[ndx]})

@app.route('/api/foundation_questions', methods=['POST'])
def get_foundation_questions():
    print(f'getting foundation questions')
    data = request.get_json()
    #print(data)
    ndx = data['question_ndx']
    return jsonify({'question': questions.foundation_questions[ndx]})

@app.route('/api/project_questions', methods=['POST'])
def get_project_questions():
    print(f'getting project questions')
    data = request.get_json()
    #print(data)
    ndx = data['question_ndx']
    return jsonify({'question': questions.project_questions[ndx]})

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
    app.run(debug=True)
