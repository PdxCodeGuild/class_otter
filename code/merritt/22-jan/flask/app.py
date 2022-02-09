from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    name = 'merritt'
    temperature = 45
    nums = [4,5,6]
    shopping_list = [
        {
            "description": "milk",
            "completed": False
        },
        {
            "description": "cheese",
            "completed": True
        },
        {
            "description": "yogurt",
            "completed": True
        },
    ] 
    return render_template('index.html', name=name, temperature=temperature, shopping_list=shopping_list)

@app.route('/goodbye/<string:name>/')
def goodbye(name):
    return f'''
    <h1>Goodbye World!</h1>
    <h3>See you later {name}!</h3>
    '''

app.run(debug=True)