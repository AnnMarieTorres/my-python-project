from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('home.html')

@app.route('/birthday')
def birthday():
	return 'March 6 1975'

@app.route('/greeting/<name>')
def greeting(name):
	return 'Hello %s'%name

@app.route('/add/<int:param1>/<int:param2>')
def add(param1,param2):
	return''