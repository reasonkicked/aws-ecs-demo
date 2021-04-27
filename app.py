import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



app = Flask(__name__)


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

def Test():
    pass



@app.route('/')
def hello_world():
    return 'Hello world!'



if __name__ == '__main__':
    app.run(host='0.0.0.0')
