'''
Eldon Wu
LLab 14, mini blog app using flask
March 19, 2026
'''
from flask import Flask, render_template, redirect,url_for,request
from flask_sqlalchemy import SQLAlchemy
import mysql.connector

app = Flask(__name__)

# database connection
db = mysql.connector.connect(
    host = 'localhost',
    user = 'flaskuser',
    password = 'password123',
    database = 'blogDB'
)

#creaate a tool 'cursor'to b used to run queries in db
cursor = db.cursor()

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/add_blog')
def add_blog():
    username = request.form['username']
    email = request.form['email']
    title = request.form['title']
    content = request.form['content']

    # insert into table users
    cursor.execute("INSERT INTO users(username, email) VALUES (%s, %s)", (username, email))

    db.commit()
    
    # get the id of the last row that was inserted into the database and store it in user_id
    user_id = cursor.lastrowid

    #insert data into table blog
    cursor.execute("INSERT INTO blog(user_id, title, content) VALUES (%s, %s, %s)", (user_id,title,content))
    
    db.commit()

    return redirect('/blogs')

@app.route('/blogs')
def blogs():
    cursor.execute("SELECT blog.id, users.username, blog.title, blog.content, blog.created_at FROM blog JOIN users ON blog.user_id = users.userid")

    # get all the data and store them in 'data'
    data = cursor.fetchall()

    return render_template('blog.html', blogs = data)

if __name__ == '__main__':
    app.run(debug=True)