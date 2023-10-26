# hello_flask.py
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootsrap = Bootstrap5(app)

@app.route('/')
def hello():
    s1 = '<p>Carlos G. : poggers</p>'
    s2 = '<p>Jean-luc M. : tfti'
    return s1 + s2

@app.route('/sergio')
def t_test():
    return render_template('templates.html')