# system imports
import streamlit as st

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
    st.session_state.expanders_expanded = False

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
    user_data['org_name']['a'] = st.text_input(questions['org_name']['q'])
    user_data['org_website']['a'] = st.text_input(questions['org_website']['q'])
    user_data['org_mission']['a'] = st.text_area(questions['org_mission']['q'])
    #user_data['org_audience']['a'] = st.text_input(questions['org_audience']['q'])
    #user_data['org_kpis']['a'] = st.text_area(questions['org_kpis']['q'])

with left_column.expander("Foundation Info", expanded=st.session_state.expanders_expanded):
    for key, value in questions.items():
        if value['category'] == 'foundation_info': user_data[key]['a'] = st.text_input(value['q']) if value['format'] == 'text_input' else st.text_area(value['q'])  
    #user_data['found_name']['a'] = st.text_input(questions['found_name']['q'])
    #user_data['found_alignment']['a'] = st.text_area(questions['found_alignment']['q'])
    #user_data['found_request']['a'] = st.text_input(questions['found_request']['q'])

with left_column.expander("Program Info", expanded=st.session_state.expanders_expanded):
    user_data['prog_name']['a'] = st.text_input(questions['prog_name']['q'])
    user_data['prog_description']['a'] = st.text_area(questions['prog_description']['q'])
    user_data['prog_budget']['a'] = st.text_input(questions['prog_budget']['q'])
    user_data['prog_audience']['a'] = st.text_area(questions['prog_audience']['q'])
    #user_data['fund_uses']['a'] = st.text_input(questions['fund_uses']['q'])
    user_data['prog_activities']['a'] = st.text_area(questions['prog_activities']['q'])
    user_data['prog_outcomes']['a'] = st.text_area(questions['prog_outcomes']['q'])
    #user_data['prog_partners']['a'] = st.text_input(questions['prog_partners']['q'])
    user_data['prog_timeline']['a'] = st.text_area(questions['prog_timeline']['q'])

with left_column.expander("Additional Info", expanded=st.session_state.expanders_expanded):
    user_data['add_info']['a'] = st.text_area(questions['add_info']['q'])


# Add a "Generate LOI" button on the left column
with left_column:
    st.markdown('<div class="center-button">', unsafe_allow_html=True)
    if st.button("Generate LOI"):
        collapse_all_expanders()
        with right_column:  # Display the output in the right column
            with st.chat_message('generator'):
                #st.write("LOI generation in progress...")
                for key, val in user_data.items():
                    if 'a' in val: st.write(f'{key}:\n\t {val['a']}')   
                #result = submit_answer(user_data, user_id)
                #st.write(result)
    st.markdown('</div>', unsafe_allow_html=True)