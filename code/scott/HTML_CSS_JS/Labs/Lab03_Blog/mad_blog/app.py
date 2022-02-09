# save this as app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html", posts=posts)

posts = [
    {   'title': "french press pumpkin spice percolator.",
        'author': "Irish americano",
        'date': "June 10th, 1896",
        'body': "beans eu grinder galão rich espresso frappuccino aromatic macchiato aftertaste. ",
    },
    
     {
        'title': "pumpkin spice percolators and fair trade blue mountain.",
        'author': " americano skinny",
        'date': "June 10th, 1931",
        'body': "siphon roast crema caramelization froth.",
    },
    {
        'title': "kopi-luwak sweet and robust.",
        'author': "galão",
        'date': "June 10th, 1931",
        'body': "Chicory at sweet a sweet rich redeye.",        
    },
    {
        'title': "Acerbic spoon,",
        'author': " et lungo",
        'date': "June 10th, 1794",
        'body': " Black rich aged et decaffeinated.",
    }
]

app.run(debug=True)