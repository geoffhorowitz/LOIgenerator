# system imports
import datetime
import sys, os
import dotenv
import google.generativeai as genai

# local imports
sys.path.append('../general_utils')
from filesystem_utils import write_json_file, write_text_file
dotenv.load_dotenv(dotenv.find_dotenv())

def simple_interface():
    genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))

    model = genai.GenerativeModel('models/gemini-1.5-flash')
    response = model.generate_content("Please give me python code to sort a list.")
    print(response.text)

class Gemini_Wrapper:
    def __init__(self, model_name=None, system_prompt=None, save_conversation=True):
        self.save_conversation = save_conversation
        #self.history = []
        self.system_prompt = 'You are a friendly assistant' if not system_prompt else system_prompt
        self.model_name = model_name if model_name else "gemini-1.5-flash"
        self.token_usage = 0

        genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))
        self.model = genai.GenerativeModel(model_name=self.model_name, system_instruction=self.system_prompt)
        self.chat = self.model.start_chat()


        print('LLM model ready')

    def __call__(self, input):
        return self.run_inference(input)
    
    
    def run_inference(self, user_text):
        count=self.model.count_tokens(user_text) # need to include system prompt???
        print(count)
        #self.token_usage += 

        print('querying model...')
        response = self.chat.send_message(user_text)
        try:
            #self.token_usage += response.result.total_token_count
            #print(response)
            #print(response.result)
            #print(response._result)
            print("Total Tokens:")
            print(response.total_token_count)
            #print(response._result["usage_metadata"]["total_token_count"])
        except Exception as e:
            pass

        #return response._result["part"]["text"]
        return response.text

    #def append_text(self, text_to_append):
    #    self.history.append(text_to_append)
    #    return self.history

    def shutdown(self):
        try:
            if self.save_conversation:
                # Find the last "/" and take only the text after it.
                save_timestamp = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
                save_loc = f"./logs/loi_{self.model_name}_{save_timestamp}.json"
                #write_json_file(save_loc, self.chat.history)
                write_text_file(save_loc, str(self.chat.history))
                write_text_file(save_loc[-5]+'_tokens.txt', self.token_usage)
        except Exception as e:
            print('Error saving data: ')
            print(e)


if __name__ == "__main__":
    kwargs = {
        'model_name': None, #use default
        'save_conversation': True,
    }
    client = Gemini_Wrapper(**kwargs)
    prompt = 'Tell me a story about a dog and a bird who become friends'
    client.run_inference(prompt)
    client.shutdown()