# system imports
import streamlit as st
import time

# local imports
from backend import get_questions, submit_answer, loi_generator, submit_feedback  #, get_generated_image
from style import *

# variable initializations
questions = get_questions()
user_id = 'test_user'

# app configs
st.set_page_config(layout="wide")

# Load CSS styles from style.py
st.markdown(load_css(), unsafe_allow_html=True)

# Session state initializations
if 'loi_generated' not in st.session_state: 
    st.session_state.loi_generated = False  # Initially, the LOI is not generated

if 'ndx_counter' not in st.session_state:
    st.session_state.ndx_counter = 0

if 'user_data' not in st.session_state:
    user_data = questions.copy()

if 'expanders_expanded' not in st.session_state: # Initialize session state to manage expander visibility
    st.session_state.expanders_expanded = True  # Initially expanded


# Function definitions
def collapse_all_expanders():
    if st.session_state.expanders_expanded:
        st.session_state.expanders_expanded = False

def generate_input_layout():
    titles = ['Organization Info', 'Foundation Info', 'Project Info', 'Additional Info']
    tags = ['org_info', 'foundation_info', 'project_info', 'additional_info']
    for title, tag in zip(titles, tags):
        with st.expander(title, expanded=st.session_state.expanders_expanded):
            for key, value in questions.items():
                if value['category'] == tag:
                    ndx = f'{st.session_state.ndx_counter}'
                    user_data[key]['a'] = st.text_input(value['q']) if value['format'] == 'text_input' else st.text_area(value['q'])
                    st.session_state.ndx_counter += 1 

@st.dialog("Provide Feedback")
def provide_feedback():
    name = st.text_input("Your Name")
    email = st.text_input("Email Address")
    message = st.text_area("Message")
    submit_feedback_button = st.button("Submit Feedback")

    if submit_feedback_button:
        if name and email and message:
            submit_feedback(name, email, message)
            st.success("Thank you for your feedback!")
            show_feedback_form.empty()  # Clear the feedback form
        else:
            st.error("Please fill in all fields.")


# Add Logo, App Title, and user's next steps buttons
st.balloons()  # Add space at the top for buttons
logo_column, title_column, hire_button, feedback_button  = st.columns([1, 7, 1, 1])  # Adjust the ratio as needed for desired spacing

with logo_column:
    st.image("../assets/GG_logo.png", width=100)
    #st.markdown(logo_html(), unsafe_allow_html=True)

with title_column:
    #st.title("Generosity AI")
    st.markdown(title_html("Generosity AI"), unsafe_allow_html=True)

# Hire a professional button
with hire_button:
    st.button("Hire a Professional", on_click=lambda: st.write(f"[Visit Generosity Genius](www.generositygenius.org)"))

# Provide feedback button
with feedback_button:
    if st.button("Provide Feedback"):
        provide_feedback()


placeholder = st.empty()
question_input = placeholder.container()

# Initial layout logic
if not st.session_state.loi_generated:
    with question_input:
        st.markdown(subtitle_html("LOI Generator"), unsafe_allow_html=True)

        generate_input_layout()
        
        # Add a "Generate LOI" button
        if st.button("Generate LOI"):
            st.session_state.loi_generated = True  # Update state to show the new layout
            collapse_all_expanders()
            st.rerun()


# After LOI generation, show the split-screen layout
if st.session_state.loi_generated:
    placeholder.empty() # clears the above layout
    left_column, right_column = st.columns([2, 2])

    #left_column = question_input
    with left_column:
        st.markdown(subtitle_html("LOI Generator"), unsafe_allow_html=True)

        generate_input_layout()

    with right_column:  # Display the output in the right column
            st.markdown(subtitle_html("LOI Results"), unsafe_allow_html=True)
            #with st.spinner(text='In progress'):
                #st.write("LOI generation in progress...")
                #result = submit_answer(user_data, user_id)
                #st.success('Done')

            with st.chat_message('generator'):
                for key, val in user_data.items():
                    if 'a' in val: st.write(f'{key}:\n\t {val['a']}') 
                #result = submit_answer(user_data, user_id)
                #st.write(result)
