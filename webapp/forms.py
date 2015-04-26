from flask.ext.wtf import Form
from wtforms.fields import TextField, TextAreaField, SubmitField, BooleanField, PasswordField
from wtforms.validators import Required, ValidationError, Email
from models import db, User, Courses

class SignupForm(Form):
  firstname = TextField("First name",  [Required("Please enter your first name.")])
  lastname = TextField("Last name",  [Required("Please enter your last name.")])
  email = TextField("Email",  [Required("Please enter your email address."), Email("Please enter your email address.")])
  password = PasswordField('Password', [Required("Please enter a password.")])
  submit = SubmitField()
 
  def __init__(self, *args, **kwargs):
    Form.__init__(self, *args, **kwargs)
 
  def validate(self):
    if not Form.validate(self):
      return False
     
    user = User.query.filter_by(email = self.email.data.lower()).first()
    if user:
      self.email.errors.append("That email is already taken")
      return False
    else:
      return True
 
class LoginForm(Form):
  email = TextField("Email",  [Required("Please enter your email address."), Email("Please enter your email address.")])
  password = PasswordField('Password', [Required("Please enter a password.")])
  submit = SubmitField()
   
  def __init__(self, *args, **kwargs):
    Form.__init__(self, *args, **kwargs)
 
  def validate(self):
    if not Form.validate(self):
      return False
     
    user = User.query.filter_by(email = self.email.data.lower()).first()
    if user and user.check_password(self.password.data):
      return True
    else:
      self.email.errors.append("Invalid e-mail or password")
      return False

class SearchForm(Form):
    searchBar = TextField("Search courses")
    search = SubmitField()

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)      
