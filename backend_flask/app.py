# app.py

# System imports
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
#import sqlite3

# Local imports
import loi_questions as questions
from models.llm_integrator import generate_image_from_prompt

app = Flask(__name__)
CORS(app)

fake_database = {}

questions = questions.questions

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
    print(f'{res} questions')
    return jsonify({'n_questions': res})

@app.route('/api/org_questions', methods=['POST'])
def get_org_questions():
    print(f'getting org questions')
    print(request.data)
    data = request.get_json()
    print(data)
    ndx = data['question_ndx'] if data and ('question_ndx' in data) else 0
    #print('responding with ', questions.org_questions[ndx])
    #return jsonify({'question': questions.org_questions[ndx]})
    print('responding with ', questions['org_questions'][ndx])
    return jsonify({'question': questions['org_questions'][ndx]})

@app.route('/api/foundation_questions', methods=['POST'])
def get_foundation_questions():
    print(f'getting foundation questions')
    data = request.get_json()
    #print(data)
    ndx = data['question_ndx']
    #return jsonify({'question': questions.foundation_questions[ndx]})
    return jsonify({'question': questions['foundation_questions'][ndx]})

@app.route('/api/project_questions', methods=['POST'])
def get_project_questions():
    print(f'getting project questions')
    data = request.get_json()
    #print(data)
    ndx = data['question_ndx']
    #return jsonify({'question': questions.project_questions[ndx]})
    return jsonify({'question': questions['project_questions'][ndx]})

@app.route('/api/additional_info', methods=['POST'])
def get_additional_questions():
    print(f'getting additional info questions')
    data = request.get_json()
    #print(data)
    ndx = data['question_ndx']
    #return jsonify({'question': questions.project_questions[ndx]})
    return jsonify({'question': questions['additional_info'][ndx]})

@app.route('/api/submit_answer', methods=['POST'])
def submit_answer():
    print('answer submitted')
    data = request.get_json()
    print(data)
    if data: # only breaking all this up for debugging purposes (could check all at once)
        if 'endpoint' in data:
            topic = data['endpoint']

            if 'answer_dict' in data:
                #q_ndx = data['question_ndx']
                #answer = data['answer']
                answer_dict = data['answer_dict']

                # Save answer to database here
                # for testing
                for q_ndx, answer in answer_dict.items():
                    print(f'for topic {topic}, question index {q_ndx}, saving answer to database: {answer}')
                
                # Connect to SQLite database to store data (makes it accessible to front-end)
                #conn = sqlite3.connect('questions.db')
                #c = conn.cursor()

                # temporary fake database
                for q_ndx, answer in answer_dict.items():
                    if topic in fake_database: fake_database[topic][int(q_ndx)] = answer
                    else: fake_database[topic] = {int(q_ndx): answer}
            else:
                # this is ok, just getting next route without submitting data
                pass
        else:
            print('no endpoint received')
            topic = ''
    else:
        print('no data received')
        topic = ''

    if topic == "homepage":
        next_route = 'org_questions'
    elif topic == 'org_questions':
        next_route = '/foundation_questions'
    elif topic == 'foundation_questions':
        next_route = '/project_questions'
    elif topic == 'project_questions':
        next_route = '/additional_questions'
    elif topic == 'additional_questions':
        next_route = '/loi_generator'
    elif topic == 'loi_generator':
        next_route = '/'
    else:
        next_route = '/'

    print('sending to next route: '+next_route)
    
    #return get_question()
    return jsonify({'success': True, 'next_route': next_route})

@app.route('/api/loi_generator', methods=['POST'])
def loi_generator():
    # placeholder for prompt generation
    print('registering prompt request...')
    
    # lets do a fake prompt
    fake_prompt = ''
    for topic in fake_database.keys():
        fake_prompt += f'{topic}:\n\n' 
        for q_ndx, answer in fake_database[topic].items():
            print(type(q_ndx))
            fake_prompt += f'\tQuestion: {questions[topic][q_ndx]}\n\t\t Answer: {answer}\n'
    fake_prompt+=f'\n\n'
    print('fake prompt: '+fake_prompt)

    return jsonify({'prompt': fake_prompt})

@app.route('/api/get_generated_image', methods=['POST'])
def get_generated_image():
    # just a fun placeholder method
    print('registering image request...')
    # generate an image for the mission statement
    image_prompt = questions['org_questions'][8] if ((8 in questions['org_questions']) and ('org_questions' in questions)) else 'Our mission is to help people'
    
    return generate_image_from_prompt(image_prompt)

if __name__ == '__main__':
    print('starting up app')
    app.run(debug=True)
