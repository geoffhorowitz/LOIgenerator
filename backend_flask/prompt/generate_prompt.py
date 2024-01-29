from .loi_prompt import example_input, example_output

def generate_loi_prompt(current_input):

    system_prompt = f"I want to create a letter of inquiry (LOI) for a nonprofit to send to a foundation. This LOI should have 5 parts as follows:\n1. An introduction paragraph. This paragraph introduces the nonprofit, it\'s misssion, and discusses why the nonprofit is a good fit for recieving a grant from the target foundation.\n2. Statement of need. This paragraph should discuss the target program/project to fund and why this project is necessary. It should also state the amount of funds being requested an breifly indicate how the funds will be used.\n3. Project narrative. This paragraph should describe the project in detail.\n4. Anticipated outcomes. This paragraph should specifically state what the outcomes/benefits of the project will be.\n5. Closing remarks. This paragraph should summarize the case for funding the program and touch on the value of the program to the target foundation.\n\nBelow is an example of the inputs:\n{example_input}\n\nBelow is an example of desired output:\n{example_output}\n\nHere are the inputs for the current LOI:\n{current_input}\n\nWhen you provide output, don't preamble it with commentary such as 'Here is the draft you asked for:'. Do include section headers like 'Statement of Need'"
    
    return system_prompt

def generate_loi_followup():
    user_prompts = [
        "Begin by writing the 1st section, introduction Paragraph",
        "Continue with the 2nd section, Statement of need",
        "Continue with the 3rd paragraph, Project narrative",
        "Continue with the 4th paragraph, Anticipated outcomes",
        "Finish with the final section, Closing remarks"
    ]
    return user_prompts

if __name__ == "__main__":
    print(generate_loi_prompt)
    print(generate_loi_followup)
