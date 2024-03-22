from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

from model import *

def main():
    app= Flask(__name__)
    app.config['SECRET_KEY'] = 'mykey'


    basedir = os.path.abspath(os.path.dirname(__file__))

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db = SQLAlchemy(app)

if __name__=="__main__":
    main()