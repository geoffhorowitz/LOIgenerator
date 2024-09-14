# system imports
import streamlit as st
import time

# local imports
from backend import get_questions, submit_answer, loi_generator  #, get_generated_image
from style import *

# variable initializations
questions = get_questions()
user_data = questions.copy()
user_id = 'test_user'

# app configs
st.set_page_config(layout="wide")

# Load CSS styles from style.py
st.markdown(load_css(), unsafe_allow_html=True)

# Functional initialization
if 'expanders_expanded' not in st.session_state: # Initialize session state to manage expander visibility
    st.session_state.expanders_expanded = True  # Initially expanded

def collapse_all_expanders():
    if st.session_state.expanders_expanded:
        st.session_state.expanders_expanded = False
        #st.rerun()

# Create two columns for the logo and title
logo_column, title_column = st.columns([1, 9])  # Adjust the ratio as needed for desired spacing

with logo_column:
    st.image("../assets/GG_logo.png", width=100)
    #st.markdown(logo_html(), unsafe_allow_html=True)

with title_column:
    #st.title("Generosity AI")
    st.markdown(title_html("Generosity AI"), unsafe_allow_html=True)


# Create two columns for the split screen layout
left_column, right_column = st.columns([2, 2])

# Add the app name
with left_column:
    st.markdown(subtitle_html("LOI Generator"), unsafe_allow_html=True)

with right_column:
    st.markdown(subtitle_html("LOI Results"), unsafe_allow_html=True)

# Add some subsections
with left_column.expander("Organization Info", expanded=st.session_state.expanders_expanded):
    for key, value in questions.items():
        if value['category'] == 'org_info': user_data[key]['a'] = st.text_input(value['q']) if value['format'] == 'text_input' else st.text_area(value['q']) 

with left_column.expander("Foundation Info", expanded=st.session_state.expanders_expanded):
    for key, value in questions.items():
        if value['category'] == 'foundation_info': user_data[key]['a'] = st.text_input(value['q']) if value['format'] == 'text_input' else st.text_area(value['q'])  

with left_column.expander("Program Info", expanded=st.session_state.expanders_expanded):
    for key, value in questions.items():
        if value['category'] == 'program_info': user_data[key]['a'] = st.text_input(value['q']) if value['format'] == 'text_input' else st.text_area(value['q'])  

with left_column.expander("Additional Info", expanded=st.session_state.expanders_expanded):
    for key, value in questions.items():
        if value['category'] == 'additional_info': user_data[key]['a'] = st.text_input(value['q']) if value['format'] == 'text_input' else st.text_area(value['q']) 


# Add a "Generate LOI" button on the left column
with left_column:
    if st.button("Generate LOI"):
        collapse_all_expanders()
        with right_column:  # Display the output in the right column
           # with st.spinner(text='In progress'):
            #    st.write("LOI generation in progress...")
                #result = submit_answer(user_data, user_id)
            #    st.success('Done')

            with st.chat_message('generator'):
                for key, val in user_data.items():
                    if 'a' in val: st.write(f'{key}:\n\t {val['a']}') 
                #result = submit_answer(user_data, user_id)
                #st.write(result)