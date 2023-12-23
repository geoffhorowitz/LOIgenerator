# app.py

# System imports
from flask import Flask, request, jsonify, send_file, send_from_directory
from flask_cors import CORS
#import sqlite3
import os, json

# Local imports
import loi_questions as questions
#from models.llm_integrator import generate_image_from_prompt
from models.anthropic_api import Claude_Wrapper
from prompt.generate_prompt import generate_loi_prompt, generate_loi_followup

app = Flask(__name__)
CORS(app)

fake_database = {}

questions = questions.questions

# to run the front-end build file
@app.route('/', defaults={'path': ''}) #route '/' handles requests to the root path. This will serve the index.html file from the React build folder by default.
@app.route('/<path:path>') #route '/path:path' handles all other paths. This will serve other files like CSS and JS files from the build folder.
def serve_react_app(path):
    return send_from_directory('../frontend_react_loi-tool/build', path)

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
    if data: # only breaking this & next line up for debugging purposes (could check all at once)
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
    
    '''
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
    '''

    # real prompt
    org_input = {}
    topic = 'org_questions'
    for q_ndx in [0, 2, 8, 9]:
        org_input[questions[topic][q_ndx]] = fake_database[topic][q_ndx] if topic in fake_database and q_ndx in fake_database[topic] else ''

    for topic in ['foundation_questions', 'project_questions', 'additional_info']:
        for q_ndx in range(len(questions[topic])):
            org_input[questions[topic][q_ndx]] = fake_database[topic][q_ndx] if topic in fake_database and q_ndx in fake_database[topic] else ''


    # testing prompt + output
    output_loi = ''
    for q, a in org_input.items():
        output_loi += f"{q}: {a}\n"

    fn = '/home/ghorowit/Desktop/github_repos/LOIgenerator/backend_flask/logs/claude-2.1_2023-12-21-00-17-33.json'
    with open(fn, "r") as f:
        raw_output = json.load(f)
    for itm in raw_output:
        if itm['role'] == 'assistant':
            output_loi += itm['content'] + '\n\n'

    return jsonify({'loi_data': output_loi})

    # real output
    output_loi = f"Dear Trustees of the {fake_database['foundation_questions'][0]}\n\n" if ('foundation_questions' in fake_database and 0 in fake_database['foundation_questions']) else "To whom it may concern\n\n"
    client = Claude_Wrapper()
    prompt = generate_loi_prompt(org_input)
    client.set_system_prompt(prompt)
    for followup in generate_loi_followup():
        #print(followup)
        output_loi += client.run_inference(followup)
    client.shutdown()

    # TODO
    # placeholder for KPIs, additional information, etc

    topic = 'org_questions'
    output_loi+='\nWarm Regards,\n'
    output_loi+=f'{fake_database[topic][4]}\n' if topic in fake_database and 4 in fake_database[topic] else ''
    output_loi+=f'{fake_database[topic][5]}\n' if topic in fake_database and 5 in fake_database[topic] else ''
    output_loi+=f'{fake_database[topic][0]}\n' if topic in fake_database and 0 in fake_database[topic] else ''

    print('LOI Result: '+output_loi)
    return jsonify({'loi_data': output_loi})


@app.route('/api/get_generated_image', methods=['POST'])
def get_generated_image():
    # just a fun placeholder method
    print('registering image request...')
    # generate an image for the mission statement
    image_prompt = questions['org_questions'][8] if ((8 in questions['org_questions']) and ('org_questions' in questions)) else 'Our mission is to help people'
    
    #return jsonify({'image_url': generate_image_from_prompt(image_prompt)})
    #image_path = os.path.join(os.getcwd(), '../assets/astronaut.png')
    image_path = '/home/ghorowit/Desktop/github_repos/LOIgenerator/frontend_react_loi-tool/images/astronaut.png'
    print('sending '+image_path)
    return jsonify({'image_url': image_path})

if __name__ == '__main__':
    print('starting up app')
    app.run(debug=False)
