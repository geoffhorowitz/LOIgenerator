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
`npm start`
or to define port:
`PORT=8000 npm start`

### runtime - build and run from backend
#### go into the react folder and build the frontend
cd frontend_react_loi-tool
npm run build

#### copy the build into the flask folder
cp -r react-app/build flask-app/

## Back-end (flask)
cd backend_flask/
python app.py


# Deployment
for deployment, will use gunicorn optimized performance. Gunicorn takes your Flask app and runs it in a production-grade server process for serving real user traffic, as opposed to Flask's development server which is meant for development/testing. It's a robust WSGI server optimized for Python.

to run: `gunicorn --bind 0.0.0.0:5000 app:app` # runs the app.py file app server <app.py:app> on port 5000
