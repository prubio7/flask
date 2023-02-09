#!/usr/bin/env python3

from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.before_request
def before_request():
	print('Antes de la petición...')

@app.after_request
def after_request(response):
	print('Después de la petición')
	return response

@app.route('/')
def index():
	array = ['Tomate','Lechuga','Queso','Pan','Huevos','Agua']
	data = {
		'title':'Lista de la compra',
		'date':'Esta tarde',
		'length':len(array)
	}

	return render_template('index.html',array=array,data=data)

@app.route('/contact/<contact>/<int:age>')
def contact(contact,age):
	data = {
		'contact':contact,
		'age':age
	}

	return render_template('contact.html',data=data)

def not_found(error):
	return render_template('404.html')
	#return redirect(url_for('index'))


if __name__ == '__main__':
	app.run(debug=True,host='0.0.0.0',port=80)
	app.register_error_handler(404,not_found)