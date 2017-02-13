from flask import Flask, render_template,jsonify
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


####Extra Credit not mine####

@app.route('/add/<int:num1>/<int:num2>')
def add(num1,num2):
	total= num1+num2
	return render_template('calcResult.html',total=str(total))
	
@app.route('/mult/<int:num1>/<int:num2>')
def mult(num1,num2):
	total=num1*num2
	return render_template('calcResult.html',total=str(total))

@app.route('/sub/<int:num1>/<int:num2>')
def sub(num1,num2):
	total= num1-num2
	return 'total %s'%str(total)
	#return render_template('calcResult.html',total=str(total))

@app.route('/favoritefood')
def favoritefoods():
	myFavFood=[
	"pizza",
	"french fries",
	"steak"
	]
	return jsonify(myFavFood)

