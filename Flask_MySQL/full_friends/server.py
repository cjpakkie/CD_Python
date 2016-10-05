from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
app = Flask(__name__)
app.secret_key = 'secretmcsecretface'
Email_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
mysql = MySQLConnector(app,'friends')

queries = {
    'show_all' : 'SELECT * FROM friends',
    'create': 'INSERT INTO friends (first_name, last_name, email, created_at, updated_at) VALUES (:first_name, :last_name, :email, NOW(), NOW())',
    'show': 'SELECT * FROM friends WHERE id = :id',
    'update': 'UPDATE friends SET first_name =:first_name, last_name=:last_name, email=:email WHERE id =:id',
    'delete': 'DELETE FROM friends WHERE id=:id'
}

@app.route('/')
def index():
    friends = mysql.query_db(queries['show_all'])
    return render_template('index.html', friends=friends)

@app.route('/friends', methods=['POST'])
def create():
    data = {
        'first_name': request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email': request.form['email']
    }
    mysql.query_db(queries['create'],data)
    return redirect('/')

@app.route('/friends/<id>', methods=['POST'])
def update(id):
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'id': id
    }
    mysql.query_db(queries['update'],data)
    return redirect('/')

@app.route('/friends/<id>/edit', methods=['GET'])
def edit(id):
    data ={
        'id': id
    }
    friend = mysql.query_db(queries['show'],data)[0]
    return render_template('edit.html', friend=friend)

@app.route('/friends/<id>/delete', methods=['POST'])
def delete(id):
    data = {
        'id':id
    }
    mysql.query_db(queries['delete'],data)
    return redirect('/')

app.run(debug=True)
