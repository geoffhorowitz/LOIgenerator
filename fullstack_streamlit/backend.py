# app.py

# System imports
import sqlite3
import sys, os, json
import hashlib

# Local imports
import loi_questions
#from models.llm_integrator import generate_image_from_prompt
from google_api import Gemini_Wrapper
from generate_prompt import generate_loi_prompt, generate_loi_followup
sys.path.append('../general_utils')
from filesystem_utils import write_text_file
from db_utils import init_db, save_to_db

fake_database = {}
db_name = 'loi_app.db'
db_path = os.path.join(os.getcwd(), 'database', db_name)
#db_path = os.path.join(os.getcwd(), db_name)
os.makedirs(os.path.dirname(db_path), exist_ok=True) # Ensure the directory exists

def get_questions():
    return loi_questions.questions


# Generate a unique identifier using user_identifier (could be an email, username, etc.)
def generate_user_id(user_identifier: str) -> str:
    return hashlib.sha256(user_identifier.encode()).hexdigest()


# The submit_answer function
def submit_answer(data: dict, user_identifier: str):
    user_id = generate_user_id(user_identifier)  # Generate a unique ID for the user

    # Store the user data in the SQLite database
    save_to_db(db_path, user_id, data)

    # Call the loi_generator function to create the LOI
    loi_text = loi_generator(data)  # Assuming this function returns a string LOI

    return loi_text


def loi_generator(data: dict):
    print('registering prompt request...')
    questions = get_questions()

    # real prompt
    org_input = {}
    for key, value in questions.items():
        org_input[value['short_desc']] = data[key]['a'] if 'a' in data[key] else ''
    
    # real output
    output_loi = f"Dear Trustees of the {data['org_name']['a']}\n\n" if 'a' in data['org_name'] else "To whom it may concern\n\n"
    prompt = generate_loi_prompt(org_input)
    client = Gemini_Wrapper(system_prompt = prompt)
    for followup in generate_loi_followup():
        # TODO: add a yield here?
        #print(followup)
        output_loi += client.run_inference(followup)
        break
    client.shutdown()

    # TODO
    # placeholder for KPIs, additional information, etc

    output_loi+='\nWarm Regards,\n'
    output_loi+=f'{data['user_name']['a']}\n' if 'a' in data['user_name'] in data else ''
    output_loi+=f'{data['user_title']['a']}\n' if 'a' in data['user_title'] in data else ''
    output_loi+=f'{data['org_name']['a']}\n' if 'a' in data['org_name'] in data else ''

    print('LOI Result: '+output_loi)
    return output_loi


def get_generated_image(data: dict):
    # just a fun placeholder method
    print('registering image request...')

    # generate an image for the mission statement
    #image_prompt = data['org_mission'] if 'org_mission' in data else 'Our mission is to help people'    
    #return generate_image_from_prompt(image_prompt)
    
    image_path = '/home/ghorowit/Desktop/github_repos/LOIgenerator/frontend_react_loi-tool/images/astronaut.png'
    print('sending '+image_path)
    return image_path


def submit_feedback(name, email, message):
    # TODO: send email
    save_timestamp = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    save_loc = f"./feedback/loi_app_{save_timestamp}.txt"
    write_text_file(save_loc, f'Name: {name}\nEmail: {email}\nMessage: {message}')
    
if __name__ == '__main__':
    print('starting up app')
