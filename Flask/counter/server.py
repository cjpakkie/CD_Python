from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

count = 0
@app.route('/')
def counter():
    session['count'] += 1
    return render_template('index.html', count = session['count'])

@app.route('/ninja', methods=['POST'])
def plustwo():
    session['count'] += 1
    return redirect('/')

@app.route('/hacker', methods=['POST'])
def reset():
    session['count'] = 0
    return redirect('/')

app.run(debug=True)
