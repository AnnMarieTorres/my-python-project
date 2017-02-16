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
	except:
		result = ('Database error')
	finally:
		return jsonify(result)
		connection.close()


@app.route('/search')
def search():
	conn = sqlite3.connect('database.db')
	cur=conn.cursor()
	try:
		name = (request.args.get('name'),)
		cur.execute('SELECT * FROM foods WHERE name=?',name)
		conn.commit()
		result = cur.fetchall()
	except:
		result =('Database Error')
	finally:
		return jsonify(result)
		conn.close()


@app.route('/drop')
def drop():
	conn = sqlite3.connect('database.db')
	cur=conn.cursor()
	try:
		cur.execute('DROP TABLE foods')
		conn.commit()
		result=('table dropped')
	except:
		conn.rollback()
		result=('Database Error')
	finally:
		return render_template('result.html',message=result)
		conn.close()


