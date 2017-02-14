#this is a flask app
from flask import Flask

app = Flask(__name__)
#####################
#__ called a dunder (double underscore)


#setting up urls
#@app.route('/')   ---- setting up a route
#def somename():   ---- function that tells the route what to do
# return 'hello'

@app.route('/')
def index():
	return app.send_static_file('home.html')

@app.route('/about')
def about():
	return 'this is my about page'

@app.route('/something')
def something():
	return'<h1>This is a html h1 tag</h1>'

@app.route('/post/<int:postnum>')
def post1(postnum):
	return 'this is post %d'%postnum







