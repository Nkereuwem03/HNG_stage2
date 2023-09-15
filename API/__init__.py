from flask import Flask
from .models import Person
from .extensions import db


def create_app(database_uri='sqlite:///database.db'):
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "secretkey"
    app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
    db.init_app(app)

    from API.main.routes import main
    app.register_blueprint(main)

    with app.app_context():
        db.create_all()

    return app
