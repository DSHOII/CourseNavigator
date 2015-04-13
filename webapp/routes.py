from webapp import app
from flask import Flask, render_template

from models import db

# Mapping the URL / to the function home(). When someone visits / then home() will execute
# home() is using the render_template function to render the template home.html
@app.route('/')
def landingpage():
  return render_template('home.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/courses')
def courses():
    return render_template('courses.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/login')
def login():
    return render_template('login.html')

# Routing for testing if the database is working
@app.route('/testdb')
def testdb():
  if db.session.query("1").from_statement("SELECT 1").all():
    return 'It works.'
  else:
    return 'Something is broken.'
