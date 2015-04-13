from flask import Flask
 
app = Flask(__name__)

# Tells Flask to use the database 'development'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysqlpw@localhost/development'

# We import db, the usable instance of the SQLAlchemy class we created in models.py, and binds it to our app
# Now db knows that it has to use the development database, and we can query it through our db-object
from models import db
db.init_app(app)
 
import webapp.routes
