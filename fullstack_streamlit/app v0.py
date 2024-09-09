import streamlit as st

from backend import submit_answer, loi_generator  #, get_generated_image
from loi_questions import questions

user_data = questions.copy()


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
    org_name = st.text_input("What is your organization's name?")
    org_website = st.text_input("What is your organization's website?")
    org_mission = st.text_area("What is your organization's mission?")
    #org_target_population = st.text_input("Who is the organization\'s target population?")
    #org_kpis = st.text_area("Please provide any key performance indicators (KPIs) you wish to highlight in this LOI")

with left_column.expander("Foundation Info"):  
    found_name = st.text_input("Who are you sending an LOI to?")
    found_alignment = st.text_area("What are the Foundation\'s major funding area(s) for which you see alignment with your grant request?")
    found_request = st.text_input("How much money are you seeking from this foundation?")

with left_column.expander("Program Info"):
    prog_name = st.text_input("What is the name of the project/program you need to fund?")
    prog_description = st.text_area("Please provide a description of this project/program")
    prog_budget = st.text_input("What is the program budget?")
    prog_audience = st.text_input("Who is your target audience?")
    prog_activities = st.text_area("What are the program activities?")
    prog_outcomes = st.text_area("What are the program's expected outcomes?")
    #prog_partners = st.text_input("Do you have partners in this program?")
    prog_timeline = st.text_area("Please provide project/program timeline (e.g., dates, length, etc.)")

with left_column.expander("Additional Info"):
    add_info = st.text_area("Is there any additional information you want to include in the LOI?")


# Add a "Generate LOI" button on the left column
if left_column.button("Generate LOI"):
    with right_column:  # Display the output in the right column
        st.write("LOI generation in progress...")  # Placeholder for the actual LOI generation logic
        # ... (Your LOI generation logic here)