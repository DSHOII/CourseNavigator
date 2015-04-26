from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash
 
db = SQLAlchemy()

# Class to model a user with attributes; first name, last name, email, and password.
class User(db.Model):
  __tablename__ = 'users'
  uid = db.Column(db.Integer, primary_key = True)
  firstname = db.Column(db.String(100))
  lastname = db.Column(db.String(100))
  email = db.Column(db.String(120), unique=True)
  pwdhash = db.Column(db.String(54))
   
  def __init__(self, firstname, lastname, email, password):
    self.firstname = firstname.title()
    self.lastname = lastname.title()
    self.email = email.lower()
    self.set_password(password)
     
  def set_password(self, password):
    self.pwdhash = generate_password_hash(password)
   
  def check_password(self, password):
    return check_password_hash(self.pwdhash, password)

# Class to model a course with attributes; title, placement, language, level, link, ects, year
class Courses(db.Model):
  __tablename__ = 'Courses'
  placement = db.Column(db.String(50), primary_key = True)
  title = db.Column(db.String(200), primary_key = True)
  language = db.Column(db.String(50))
  level = db.Column(db.String(50))
  link = db.Column(db.String(100))
  ects = db.Column(db.String(10))
  year = db.Column(db.String(50), primary_key = True)













