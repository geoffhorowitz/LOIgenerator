from huggingface_hub import InferenceClient
from flask import jsonify, send_file
from PIL import Image
import datetime

#image = client.text_to_image("An astronaut riding a horse on the moon.")
#image.save("astronaut.png")

def generate_image_from_prompt(prompt):
    #default_model = "prompthero/openjourney-v4"
    #model_stable_diffusion = "runwayml/stable-diffusion-v1-5"

    #client = InferenceClient(model="prompthero/openjourney-v4")

    #image = client.text_to_image(prompt)
    
    # for send_file method, need to save the file and provide the location
    #loc = f"./image_{datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"
    #image.save(loc)
    
    # for testing
    loc = r'C:\Users\Geoffrey\Desktop\github_repos\LOItool\backend_flask\astronaut.png'
    #image = Image.open(r'C:\Users\Geoffrey\Desktop\github_repos\LOItool\backend_flask\astronaut.png')
    
    '''
    # get image in bytes
    image_bytes = list(image.tobytes())

    # Create JSON object with image bytes and metadata
    image_data = {
        'bytes': image_bytes, 
        'size': image.size,
        'mode': image.mode
    }
    '''
    print(loc)
    image_data = send_file(loc)
    print(image_data)

    return image_data