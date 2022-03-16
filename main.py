#first steps
from flask import Flask, request
from requests import get
from api import download_summary, download_confirmed_per_country

import logging
log_format = "[%(levelname)s] - %(asctime)s : %(message)s in %(module)s:%(lineno)d"
logging.basicConfig(filename='covid.log', format=log_format, level=logging.INFO)

server = Flask('covid dashboard')
@server.route('/')

def index():
  return "a nice covid dashboard"


#define summary route
@server.route('/summary')

def serve_summary():
  return download_summary()
  

@server.route('/new')

def serve_summary_new():
  return "A pie chart summary of new COVID cases globally."


@server.route('/netherlands')

def serve_netherlands_history():
  return download_confirmed_per_country("netherlands")




server.run('0.0.0.0')  