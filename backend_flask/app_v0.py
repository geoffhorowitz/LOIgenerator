'''
Author: Geoff Horowitz
Date: Oct 2023

Description:
This is the main app page for an LOI creation tool

Run Instructions:

Open http://localhost:5000/ to see the home page.
Open http://localhost:5000/submit to see the submit answer page.
'''

from flask import Flask, render_template, request, redirect, send_from_directory
import sqlite3

app = Flask(__name__)

# Connect to SQLite database to store data (makes it accessible to front-end)
conn = sqlite3.connect('questions.db')
c = conn.cursor()

# to run the front-end build file
'''
@app.route('/<path:path>')
def serve_react_app(path):
    return send_from_directory('build', path)
'''
# @app.route decorator defines the routes to the specific pages
@app.route('/')
def home():
    #return "Home Page" # for testing, just returning a string now instead of the actual page
    return render_template('home.html')

# Endpoint to receive and store submitted answer
@app.route('/api/submit_answer', methods=['POST'])
def submit_answer():
  answer = request.form['answer']

  # Store answer in database
  c.execute("INSERT INTO answers (answer) VALUES (?)", (answer,))
  conn.commit()

  # Redirect to home page with next question
  return redirect('/')

@app.route('/api/question')
def page2():
    # Fetch and display next question
    question = "Question 2: What is the capital of Italy?"
    return render_template('home.html', question=question)

@app.route('/submit')
def submit():
    return render_template('submit.html')

if __name__ == '__main__':
   app.run()
