from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
app = Flask(__name__)
app.secret_key = "SuperDuperSecretMcSecretFace"
Email_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
mysql = MySQLConnector(app,'emailvalidate')

queries = {
    'create': 'INSERT INTO emails (email, created_at) VALUES (:email, NOW())',
    'display': 'SELECT * FROM emails',
    'delete': 'DELETE FROM emails WHERE id = :id'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success')
def show():
    everything = mysql.query_db(queries['display'])
    return render_template('success.html', everything=everything)

@app.route('/process', methods=['POST'])
def process():
    email = request.form['email']
    if not Email_REGEX.match(email):
        flash("Email Is Not Valid")
        return redirect('/')
    else:
        flash("Email is Valid!")
        query = queries['create']
        data = {
            'email': email
        }
        mysql.query_db(query,data)
        return redirect('/success')

@app.route('/delete/<email_id>')
def delete(email_id):
    query = queries['delete']
    data = {'id': email_id}
    mysql.query_db(query,data)
    return redirect('/success')

app.run(debug=True)
