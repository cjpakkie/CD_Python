from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'friendsdb')
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/riends', methods=['POST'])
def create():
    #add a friend to the database!
    return redirect('/')
app.run(debug=True)
