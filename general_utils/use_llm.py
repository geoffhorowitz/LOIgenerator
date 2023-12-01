import sys

# local imports
sys.path.append('../backend_flask/models')
from llm_test import LLM_Wrapper, Llama_Wrapper
from chatbot_window import ChatbotApp

kwargs = {
    'model_name': None, #use default
    'use_history': False,
    'save_conversation': True,
}
#llm_instance = LLM_Wrapper(**kwargs)
llm_instance = Llama_Wrapper(**kwargs)
ChatbotApp(response_model=llm_instance)
llm_instance.shutdown()