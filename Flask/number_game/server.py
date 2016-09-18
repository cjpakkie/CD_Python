from flask import Flask, render_template, request, redirect, session
from random import randrange
app = Flask(__name__)
app.secret_key = 'lalalarandom'

@app.route('/')
def index():
    if 'answer' not in session:
        session['answer'] =  randrange(1,101)
        session['result'] = 'Make a guess'
    return render_template ('index.html')

@app.route('/guess', methods=["POST"])
def guess():
    guess = int(request.form['guess'])
    if session['answer'] == guess:
        session['result'] = 'YOU ARE CORRECT'
    elif session['answer'] > guess:
        session['result'] = 'TOO LOW'
    else:
        session['result'] = 'TOO HIGH'
    return redirect('/')

@app.route('/reset')
def reset():
    session.pop('answer')
    return redirect('/')

app.run(debug=True)
