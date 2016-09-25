from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)
app.secret_key = 'teenagemutantninjaturtles'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def ninja():
    #show all turtles
    return render_template('ninja.html', turtles = 'cowabunga')

@app.route('/ninja/<turtles>')
#change <turtles> into designated color
def turtles(turtles):
    colors = ['blue', 'orange', 'red', 'purple']
    for color in colors:
        if color == turtles:
            return render_template('ninja.html', turtles=turtles)
    #april
    return render_template('ninja.html', turtles='april')

app.run(debug=True)
