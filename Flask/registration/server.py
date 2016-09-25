from flask import Flask, redirect, request, session, render_template, flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

app = Flask(__name__)
app.secret_key = 'registrationsecretstuff'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def registration():
    if len(request.form['first_name']) < 1:
        flash('First Name cannot be blank')
    elif not request.form['first_name'].isalpha():
        flash('First Name cannot contain numbers')
    if len(request.form['last_name']) < 1:
        flash('Last Name cannot be blank')
    elif not request.form['last_name'].isalpha():
        flash('Last Name cannot contain numbers')
    if len(request.form['email']) <1 :
        flash('Email cannot be blank')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
    if len(request.form['password']) < 8:
        flash('Password must be greater than 8 characters')
    if len(request.form['password']) != len(request.form['password_confirm']):
        flash('Passwords do not match')
    else:
        flash('You have successfully registered!')
    return redirect('/')

app.run(debug=True)
