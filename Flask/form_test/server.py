from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
@app.route('/')
def index():
  return render_template("index.html")

@app.route('/users', methods=['POST'])
def create_user():
   print "Got Post Info"
   session['name']= request.form['name']
   session['email'] = request.form['email']
   # redirects back to the '/' route
   return redirect('/show')

@app.route('/show')
def show_user():
    return render_template('user.html', name=session['name'], email=session['email'])
app.run(debug=True) # run our server
