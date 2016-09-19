from flask import Flask, render_template, request, redirect, session
from random import randint
import datetime
app = Flask(__name__)
app.secret_key = 'lalalarandom'

@app.route('/')
def index():
    if 'total' not in session:
        session['total'] = 0
        session['activity'] =[]
    print session['total']
    print session['activity']
    return render_template('/index.html')

@app.route('/proccess_money', methods=["POST"])
def calculate_money():

    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    hiddeninput = request.form['hidden']
    if hiddeninput == 'farm':
        location = 'farm'
        session['profit'] = randint(10,20)
        session['total'] += session['profit']
        print datetime.datetime.now
    elif hiddeninput == 'cave':
        location = 'cave'
        session['profit'] = randint(5,10)
        session['total'] += session['profit']
    elif hiddeninput == 'house':
        location = 'house'
        session['profit'] = randint(2,5)
        session['total'] += session['profit']
    elif hiddeninput == 'casino':
        location = 'casino'
        session['profit'] = randint(-50,50)
        session['total'] += session['profit']

    if location == 'casino' and session['profit'] > 0:
        session['activity'].append('Entered a casino and won ' + str(session['profit']) + ' gold!' +' '+ str(date))
    elif location == 'casino' and session['profit'] < 0:
        session['activity'].append('Entered a casino and lost ' + str(session['profit']) + ' gold...ouch..' +' '+ str(date))
    else:
        session['activity'].append('Earned ' + str(session['profit']) + ' gold from the ' + location + ' ' + str(date))
    return redirect('/')


@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')
app.run(debug=True)
