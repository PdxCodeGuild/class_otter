from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'title': "french press pumpkin spice percolator.",
        'author': "Irish americano",
        'date': "June 10th, 1896",
        'body': "beans eu grinder galão rich espresso frappuccino aromatic macchiato aftertaste. ",
    }

     {
        'title': "pumpkin spice percolators and fair trade blue mountain.",
        'author': " americano skinny",
        'date': "June 10th, 1931",
        'body': "siphon roast crema caramelization froth.",
    }

    {
        'title': "kopi-luwak sweet and robust.",
        'author': "galão",
        'date': "June 10th, 1931",
        'body': "Chicory at sweet a sweet rich redeye.",        
    }

    {
        'title': "Acerbic spoon,",
        'author': " et lungo",
        'date': "June 10th, 1794",
        'body': " Black rich aged et decaffeinated.",
    }
]

posts1 = []


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