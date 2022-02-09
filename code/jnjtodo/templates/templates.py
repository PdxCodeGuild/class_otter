from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    name = 'bob'
    temperature = 67
    nums = [1, 2, 3]  
    return render_template('index.html', name=name, temperature=temperature, nums=nums)