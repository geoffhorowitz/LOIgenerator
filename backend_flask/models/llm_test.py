# system imports
from huggingface_hub import InferenceClient
import datetime
import sys, os
import dotenv

# local imports
sys.path.append('../../general_utils')
from filesystem_utils import write_json_file
#dotenv.load_dotenv(dotenv_path="../../")
dotenv.load_dotenv(dotenv.find_dotenv())

class LLM_Wrapper:
    def __init__(self, model_name=None, use_history=False, save_conversation=False):
        self.use_history = use_history
        self.save_conversation = save_conversation
        self.history = {'conversation':{'generated_responses': [], 'past_user_inputs': []}}

        if not model_name:
            #self.model_name = 'tiiuae/falcon-7b-instruct' # an instruct model. Given a start, it will finish
            #self.model_name = 'microsoft/DialoGPT-large' #chatbot model
            #self.model_name='IlyaGusev/saiga_mistral_7b_lora'
            #self.model_name = 'meta-llama/Llama-2-13b-chat-hf'
            self.model_name = 'google/flan-t5-xxl'

        self.client = InferenceClient(model=self.model_name, token=os.getenv("HUGGINGFACE_API_KEY"))

        print('LLM model ready')

    def __call__(self, input):
        return self.run_inference(input)

    def system_prompt(self, system_text):
        self.run_inference(system_text)
    
    def run_inference(self, user_text):
        print('querying model...')
        if self.use_history:
            output = self.client.conversational(user_text,
                                            generated_responses=self.history["conversation"]["generated_responses"],
                                            past_user_inputs=self.history["conversation"]["past_user_inputs"],
                                            model = self.model_name)
            self.history = output
        else:
            output = self.client.conversational(user_text,
                                            model = self.model_name)

        print(f"response: {output['generated_text']}")

        return output['generated_text']

    def append_text(self, text_to_append):
        self.history += text_to_append
        return self.history

    def shutdown(self):
        if self.save_conversation:
            # Find the last "/" and take only the text after it.
            last_slash_index = self.model_name.rfind("/")
            model_save_name = self.model_name[last_slash_index + 1:]
            save_timestamp = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
            save_loc = f"./{model_save_name}_{save_timestamp}"
            write_json_file(save_loc, self.history)

#################################################################################
import requests

# Llama API doesn't work for basic HF account. it requires >10GB which is the limit for the free Inference API account
class Llama_Wrapper(LLM_Wrapper):
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.API_URL = "https://api-inference.huggingface.co/models/meta-llama/Llama-2-13b-chat-hf"
        self.headers = {"Authorization": f'Bearer {os.getenv("HUGGINGFACE_API_KEY")}'}

    def run_inference(self, user_text):
        payload = {"inputs": user_text}
        response = requests.post(self.API_URL, headers=self.headers, json=payload)
        print(response.json())
        return response.json()
    

class Flan_Wrapper(LLM_Wrapper):
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        #self.API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-xxl"
        self.API_URL = "https://api-inference.huggingface.co/models/bigscience/bloom"
        self.headers = {"Authorization": f'Bearer {os.getenv("HUGGINGFACE_API_KEY")}'}

    def run_inference(self, user_text):
        payload = {"inputs": user_text}
        response = requests.post(self.API_URL, headers=self.headers, json=payload)
        print(response.json())
        return response.json()



###############################################################################
def run_llm(model_name = None):
    if not model_name:
        model_name = 'tiiuae/falcon-7b-instruct'

    client = InferenceClient(model=model_name)

    output = client.text_generation("An astronaut riding a horse on the moon.")
    print(output)
    return output


if __name__ == "__main__":
    kwargs = {
        'model_name': None, #use default
        'use_history': False,
        'save_conversation': True,
    }
    client = Flan_Wrapper(**kwargs)
    prompt = 'Tell me a story about a dog and a bird who become friends'
    client.run_inference(prompt)