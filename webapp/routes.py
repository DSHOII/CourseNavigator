from webapp import app
from flask import Flask, render_template, request, flash, session, url_for, redirect
from forms import SignupForm, LoginForm, SearchForm

from models import db, User, Courses

# Mapping the URL / to the function home(). When someone visits / then home() will execute
# home() is using the render_template function to render the template home.html
@app.route('/', methods=['GET', 'POST'])
@app.route('/home',  methods=['GET', 'POST'])
def home():
    form = SearchForm()
        
    if request.method == 'GET':
        return render_template('home.html', form=form)
    elif request.method == 'POST':
        #courses = Courses.query.filter_by(title = form.searchBar.data).all()
        # The string manipulation is quite hacky (should use match-statement to fulltext query the database)
        # The database should support fulltext search
        courses = db.session.query(Courses).filter(Courses.title.like("%" + form.searchBar.data + "%")).all()
        #courses = db.session.query(Courses).filter(Courses.title.match(form.searchBar.data)).all()
        
        return render_template('about.html', courses=courses)
    
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/courses')
def courses():
    return render_template('courses.html')

@app.route('/profile')
def profile():
 
  if 'email' not in session:
    return redirect(url_for('login'))
 
  user = User.query.filter_by(email = session['email']).first()
 
  if user is None:
    return redirect(url_for('login'))
  else:
    return render_template('profile.html')

# Sign up page logic
@app.route('/signup', methods=['GET', 'POST'])
def signup():
  form = SignupForm()
   
  if request.method == 'POST':
    if form.validate() == False:
      return render_template('signup_bootstrap.html', form=form)
    else:
        newuser = User(form.firstname.data, form.lastname.data, form.email.data, form.password.data)
        db.session.add(newuser)
        db.session.commit()
        session['email'] = newuser.email
        return redirect(url_for('profile'))
   
  elif request.method == 'GET':
    return render_template('signup_bootstrap.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm()
  
  if 'email' in session:
    return redirect(url_for('profile'))
   
  if request.method == 'POST':
    if form.validate() == False:
      return render_template('login_bootstrap.html', form=form)
    else:
      session['email'] = form.email.data
      return redirect(url_for('profile'))
                 
  elif request.method == 'GET':
    return render_template('login_bootstrap.html', form=form)

@app.route('/signout')
def signout():
 
  if 'email' not in session:
    return redirect(url_for('login'))
     
  session.pop('email', None)
  return redirect(url_for('home'))
