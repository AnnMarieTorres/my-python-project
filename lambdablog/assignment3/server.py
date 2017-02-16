from flask import Flask, jsonify, render_template, request
import sqlite3
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/enternew')
def enternew():
	return render_template('food.html')

@app.route('/addfood', methods = {'POST'})
def addfood():
	connection=sqlite3.connect('database.db')
	cursor=connection.cursor()
	try:
		name = request.form['name']
		calories = request.form['calories']
		cuisine = request.form['cuisine']
		is_vegetarian = request.form['is_vegetarian']
		is_gluten_free = request.form['is_gluten_free']
		cursor.execute('INSERT INTO foods(name,calories,cuisine,is_vegetarian,is_gluten_free) VALUES (?,?,?,?,?)',(name,calories,cuisine,is_vegetarian,is_gluten_free))
		connection.commit()
		message = 'Record Successfully Added'
	except:
		connection.rollback()
		message = 'Error in INSERT OPERATION'
	finally:	
		return render_template('result.html',message=message)
		connection.close()


##### EXTRA CREDIT #####
@app.route('/favorite')
def favorite():
	connection=sqlite3.connect('database.db')
	cursor=connection.cursor()
	try:
		cursor.execute('SELECT * FROM foods Where name="mango"')
		connection.commit()
		result = cursor.fetchone()
		print ('try this');
	except:
		result = ('Database error')
		print ('except this');
	finally:
		return jsonify(result)
		print ('finally this');
		connection.close()


