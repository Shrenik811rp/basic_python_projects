from logging import debug
from flask import Flask,render_template

from flask_sqlalchemy import SQLAlchemy

#create an instance
app = Flask(__name__)

#path to database where the data of webpage is stored

'''
using sqlite database
sqlite:/// ->relative path so its not specific less error prone
'''
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data_bs.sqlite'


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


data_bs = SQLAlchemy(app)
'''
@app.route('/') -> will take you to location where index.html page is hosted on local host.
'''
@app.route('/')
def index():

    #render_template -> used to link html file so we can host it online
    return (render_template('index.html'))

'''
@app.route('/about') -> will take you to location where about.html page is hosted on local host.
'''
@app.route('/about')
def about():
    return "This the about page"

#to get url of webpage automatically without typing run commands on terminal

if __name__ == "__main__":
    data_bs.create_all()
    app.run(debug=True)


print("working fine...")