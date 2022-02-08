from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    name = 'Ian'
    temperature = 45
    # nums = [10, 20, 30]  
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
            "description": "butter",
            "completed": False
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