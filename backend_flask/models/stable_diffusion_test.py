from huggingface_hub import InferenceClient
default_model = "prompthero/openjourney-v4"
model_stable_diffusion = "runwayml/stable-diffusion-v1-5"

model_use = model_stable_diffusion

client = InferenceClient(model=model_use)

#image = client.text_to_image("An astronaut riding a horse on the moon.")
#image.save("astronaut.png")
image = client.text_to_image("Logo for my nonprofit grant writing management company")
image.save("logo.png")