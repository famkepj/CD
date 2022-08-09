from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return 'Hello, world!'

@app.route('/joke')
def joke():
	return 'What do you call an alligator who solves mysteries?'

@app.route('/answer')
def answer():
	return 'An investgator!'

with app.test_request_context():
	print(url_for('index'))
	print(url_for('joke'))
	print(url_for('answer'))
