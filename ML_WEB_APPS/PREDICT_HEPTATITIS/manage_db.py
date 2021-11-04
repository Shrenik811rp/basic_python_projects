import sqlite3

connection = sqlite3.connect("userdata.db")

cursor = connection.cursor()

#create a table for all users using sql syntax
def create_usertable():
    cursor.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')


#function to add user data into the table
def add_userdata(username,password):
	cursor.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
	connection.commit()

#function to create login database
def login_user(username,password):
	cursor.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
	data = cursor.fetchall()
	return data



def view_all_users():
	cursor.execute('SELECT * FROM userstable')
	data = cursor.fetchall()
	return data