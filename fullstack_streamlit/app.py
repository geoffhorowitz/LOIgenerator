import streamlit as st

from backend import get_questions, submit_answer, loi_generator  #, get_generated_image

questions = get_questions()
user_data = questions.copy()
user_id = 'test_user'

# Create two columns for the logo and title
logo_column, title_column = st.columns([1, 3])  # Adjust the ratio as needed for desired spacing

with logo_column:
    st.image("../assets/GG_logo.png", width=150)

with title_column:
    st.title("Generosity AI")

# Add the app name
st.header("LOI Generator")

# Create two columns for the split screen layout
left_column, right_column = st.columns(2)

# Add some subsections
with left_column.expander("Organization Info"):
    user_data['org_name']['a'] = st.text_input(questions['org_name']['q'])
    user_data['org_website']['a'] = st.text_input(questions['org_website']['q'])
    user_data['org_mission']['a'] = st.text_area(questions['org_mission']['q'])
    #user_data['org_audience']['a'] = st.text_input(questions['org_audience']['q'])
    #user_data['org_kpis']['a'] = st.text_area(questions['org_kpis']['q'])

with left_column.expander("Foundation Info"):
    for key, value in questions.items():
        if value['category'] == 'foundation_info': user_data[key]['a'] = st.text_input(value['q']) if value['format'] == 'text_input' else st.text_area(value['q'])  
    #user_data['found_name']['a'] = st.text_input(questions['found_name']['q'])
    #user_data['found_alignment']['a'] = st.text_area(questions['found_alignment']['q'])
    #user_data['found_request']['a'] = st.text_input(questions['found_request']['q'])

with left_column.expander("Program Info"):
    user_data['prog_name']['a'] = st.text_input(questions['prog_name']['q'])
    user_data['prog_description']['a'] = st.text_area(questions['prog_description']['q'])
    user_data['prog_budget']['a'] = st.text_input(questions['prog_budget']['q'])
    user_data['prog_audience']['a'] = st.text_area(questions['prog_audience']['q'])
    #user_data['fund_uses']['a'] = st.text_input(questions['fund_uses']['q'])
    user_data['prog_activities']['a'] = st.text_area(questions['prog_activities']['q'])
    user_data['prog_outcomes']['a'] = st.text_area(questions['prog_outcomes']['q'])
    #user_data['prog_partners']['a'] = st.text_input(questions['prog_partners']['q'])
    user_data['prog_timeline']['a'] = st.text_area(questions['prog_timeline']['q'])

with left_column.expander("Additional Info"):
    user_data['add_info']['a'] = st.text_area(questions['add_info'])


# Add a "Generate LOI" button on the left column
if left_column.button("Generate LOI"):
    result = submit_answer(user_data, user_id)
    with right_column:  # Display the output in the right column
        st.write("LOI generation in progress...")  # Placeholder for the actual LOI generation logic
        # ... (Your LOI generation logic here)