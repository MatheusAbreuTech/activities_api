from flask import Flask
from extensions import db
from controllers.pessoa_controller import pessoa_bp

def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pessoa.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)


    return app
