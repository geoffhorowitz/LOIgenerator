# LOI Generation Tool
Author: Geoff Horowitz
Initial Development Date: Oct 2023

# Purpose
LOI Generation Tool

# Installation
See [requirements file](requirements.yaml)
Also requires npm installation from [Nodejs](https://nodejs.org/en/download)

# Run Procedure
## Front-end (react)

### testing - run in debug mode

### runtime - build and run from backend
#### go into the react folder and build the frontend
cd frontend_react_loi-tool
npm run build

#### copy the build into the flask folder
cp -r react-app/build flask-app/

## Back-end (flask)
cd backend_flask/
python app.py
