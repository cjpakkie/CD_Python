from flask import Flask, render_template, request, redirect
app= Flask(__name__)

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
    return render_template('results.html', name = name, location = location, language = language, comment = comment)
app.run(debug=True)
