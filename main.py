#first steps
from flask import Flask, request

server = Flask('covid dashboard')
@server.route('/')

def index():
  return "a nice covid dashboard"


#define summary route
@server.route('/summary')

def serve_summary():
  return "A bar chart summary of COVID cases per country."
  

@server.route('/new')

def serve_summary_new():
  return "A pie chart summary of new COVID cases globally."


@server.route('/netherlands')

def serve_netherlands_history():
  return "An area chart of COVID cases over time in the Netherlands."



server.run('0.0.0.0')  