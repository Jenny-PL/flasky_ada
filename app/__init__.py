# Note: on the same level as the app folder, a migrations folder
# was set up automatically from terminal command: (1)`flask db init`:
# This is done only 1x per project.
# Other terminal commands to add Model as a Table in DB:
# (2) `flask db migrate -m "ex msg: Added Cat Model"` then (3) `flask db update`
# These last two commands will be done any time we need to update the db

from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate
from dotenv import load_dotenv # this is a function that loads the dot env
import os

# Must create objects; this allows us to use what we imported above
db = SQLAlchemy() # This creates the database object
migrate = Migrate()
load_dotenv() # calling the function we imported above

def create_app(testing=None):
    # __name__ stores the name of the module we're in (placeholder)
    app = Flask(__name__)

    # connect our database to app and tell it where it is
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False # gets rid of some little error
    if testing is None:
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_DATABASE_URI")
    else:
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("TESTING_SQLALCHEMY_DATABASE_URI")

# def create_app(testing = None):
#     # __name__ stores the name of the module we're in
#     app = Flask(__name__)

#     # This turns off some notifications we don't want:
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
#     if testing == {'testing': True}:
#     # this connects our database to sqlalchemy
#     # default PostgreSQL port is 5432
#         app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('TESTING_SQLALCHEMY_DATABASE_URI')
#     else:
#         app.config['SQLALCHEMY_DATABASE_URI']= os.environ.get('SQLALCHEMY_DATABASE_URI')

    # somehow important... to connect databse
    db.init_app(app)
    migrate.init_app(app, db) # this passes in the Flask application and db

    from .models.cats import Cat

    from .routes.cats import cats_bp
    app.register_blueprint(cats_bp)

    return app