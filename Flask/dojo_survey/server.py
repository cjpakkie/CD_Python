from flask import Flask, render_template, request, redirect, flash
app= Flask(__name__)
app.secret_key = 'thisissomesecretstuff'

@app.route('/')
def index():
    cities = ['San Jose', 'Seattle', 'New York']
    languages = ['Python', 'Ruby', 'Swift']
    return render_template('index.html', cities = cities, languages = languages)

@app.route('/results', methods=['POST'])
def results():
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    if len(name) < 1 or len(comment) < 1:
        flash('Name and comments cannot be empty.')
        return redirect('/')
    if len(comment) > 150:
        flash("Comment cannot be greater than 150 characters.")
        return redirect('/')
    else:
        return render_template('results.html', name = name, location = location, language = language, comment = comment)

app.run(debug=True)
