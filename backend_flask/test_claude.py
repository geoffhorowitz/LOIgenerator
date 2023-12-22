# local imports
from models.anthropic_api import Claude_Wrapper
from prompt.generate_prompt import generate_loi_prompt, generate_loi_followup

client = Claude_Wrapper()
prompt = generate_loi_prompt()
client.set_system_prompt(prompt)
for followup in generate_loi_followup():
    #print(followup)
    client.run_inference(followup)
client.shutdown()