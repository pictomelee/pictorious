# super simple test of flask

from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/index')

def index():
	return render_template('index.html')
#def hello_world():
#	return 'Hello World!'

if __name__ == '__main__':
	app.run(host='0.0.0.0')

