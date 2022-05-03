from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate

# Must create objects; this allows us to use what we imported above
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    # __name__ stores the name of the module we're in
    app = Flask(__name__)

    # This turns off some notifications we don't want:
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
    # this connects our database to sqlalchemy
    # default PostgreSQL port is 5432
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/cats_development'

    # somehow important... to connect databse??
    db.init_app(app)
    migrate.init_app(app, db)

    from .models.cats import Cat

    from .routes.cats import cats_bp
    app.register_blueprint(cats_bp)

    return app