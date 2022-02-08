from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/foobar')
def foobar():
    return '<h1>Hi there, foobar!</h1>'
        
app.run(debug=True)