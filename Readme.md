# LOI Generation Tool
Author: Geoff Horowitz
Initial Development Date: Oct 2023

# Purpose
LOI Generation Tool

# Installation
See [requirements file](requirements.yaml)
Also requires npm installation from [Nodejs](https://nodejs.org/en/download)

## LLM access
an environment file should be included `./.env` in the top level directory. The .env file contains secrets and keys needed for various APIs. Current API keys include:
- HUGGINGFACE_API_KEY: the API key for a huggingface InferenceClient
- ANTHROPIC_API_KEY: the API key for a Anthropic claude API access

# Run Procedure
## Front-end (react)

### testing - run in debug mode
cd frontend_react_loi-tool
npm start

### runtime - build and run from backend
#### go into the react folder and build the frontend
cd frontend_react_loi-tool
npm run build

#### copy the build into the flask folder
cp -r react-app/build flask-app/

## Back-end (flask)
cd backend_flask/
python app.py
