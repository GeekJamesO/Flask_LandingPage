from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def indexRoute():
    return render_template('index.html')

@app.route('/ninjas')
def ninjasRoute():
    return render_template('ninjas.html')

@app.route('/dojos/<param>')
def dojosRoute(param):
    return render_template('dojos.html', InParameter = param)

app.run(debug=True)
