# system imports
from huggingface_hub import InferenceClient
import datetime
import sys

# local imports
sys.path.append('../../general_utils')
from filesystem_utils import write_text_file, append_text_file

class LLM_Wrapper:
    def __init__(self, model_name=None, use_history=False, save_conversation=False):
        self.use_history = use_history
        self.save_conversation = save_conversation
        self.history = []

        if not model_name:
            #self.model_name = 'tiiuae/falcon-7b-instruct' # an instruct model. Given a start, it will finish
            self.model_name = 'microsoft/DialoGPT-large' #chatbot model

        self.client = InferenceClient(model=self.model_name)

    def __call__(self, input):
        self.run_inference(input)

    def system_prompt(self, system_text):
        self.run_inference(system_text)
    
    def run_inference(self, user_text):
        if self.use_history:
            input_text = self.append_text(user_text)
        else:
            if self.save_conversation: self.append_text(user_text)
            input_text = user_text

        output = self.client.text_generation(input_text)
        print('response:')
        print(output)

        if self.use_history or self.save_conversation:
            self.append_text(output)

        return output

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
            write_text_file(save_loc, self.history)



def run_llm(model_name = None):
    if not model_name:
        model_name = 'tiiuae/falcon-7b-instruct'

    client = InferenceClient(model=model_name)

    output = client.text_generation("An astronaut riding a horse on the moon.")
    print(output)
    return output


if __name__ == "__main__":
    use_llm()