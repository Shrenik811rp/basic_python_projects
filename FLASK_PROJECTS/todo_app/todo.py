from logging import debug
from sys import meta_path

#to refresh page use redirect
#to go back to index page
from flask import Flask,render_template,request,redirect,url_for

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
    #show all todo items
    # in the class instances 
    todo_list = Todo.query.all()

    #print(todo_list)


    #render_template -> used to link html file so we can host it online

    #to show data that is entered as tasks add todo_list=todo_list
    return (render_template('index.html',todo_list=todo_list))

'''
@app.route('/add') -> will take you to location where about.html page is hosted on local host.
'''

#the url for adding task is done using @app.route

#WE add task so we post something so POST
@app.route('/add',methods=["POST"])
def add():

    title = request.form.get("title")
    #create an instance of class Todo
    new_todo = Todo(title=title,complete_check=False)

    #add this to database
    data_bs.session.add(new_todo)

    #commit the data
    data_bs.session.commit()

    #redirect user to index page once task is added
    return redirect(url_for("index"))


#the url for adding task is done using @app.route

#WE add task so we post something so POST
@app.route('/update/<int:todo_id>')
def update(todo_id):

    todo = Todo.query.filter_by(id=todo_id).first()

    todo.complete_check = not todo.complete_check

    #commit the data
    data_bs.session.commit()

    #redirect user to index page once task is added
    return redirect(url_for("index"))

@app.route('/delete/<int:todo_id>')
def delete(todo_id):

    todo = Todo.query.filter_by(id=todo_id).first()

    data_bs.session.delete(todo)

    #commit the data
    data_bs.session.commit()

    #redirect user to index page once task is added
    return redirect(url_for("index"))


#class for todo items

#inherit data_bs model
class Todo(data_bs.Model):

    """id for task item"""
    #primary_key=True -> each task will have a unique id
    #each entry we create column
    #Data entered in column is ID which is int datatype
    id = data_bs.Column(data_bs.Integer,primary_key=True)

    """title for task name"""

    #data entered into column is of string type max length of 200 chars
    title = data_bs.Column(data_bs.String(200))

    """bool if the task is completed or not"""
    #To check if task is completed or not we use boolean type
    complete_check = data_bs.Column(data_bs.Boolean)

#to get url of webpage automatically without typing run commands on terminal

if __name__ == "__main__":
    data_bs.create_all()
    '''
    #create an instance of class Todo
    new_todo = Todo(title="task 1",complete_check=False)

    #add this to database
    data_bs.session.add(new_todo)

    #commit the data
    data_bs.session.commit()
    '''    
    app.run(debug=True)


print("working fine...")