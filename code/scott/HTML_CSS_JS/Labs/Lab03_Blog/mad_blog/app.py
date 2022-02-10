# save this as app.py
from flask import Flask, render_template, request, re

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html", posts=posts)

 Import some stuff from flask.
from flask import Flask, render_template, request, redirect

# Import JsonDB 'class' from jsondb 'module'.
from jasondb import JsonDB

# Create Flask object.
app = Flask(__name__)

# Create JsonDB object.
db = JsonDB('db.json')
db.load()

# Get a todo from the database.
todo_list = db.get('todos')

@app.route('/', methods=['GET', 'POST'])
def index():
    
    if request.method == 'POST':
        
        todo_text = request.form['text']
        priority = request.form['priority']
        print(todo_text)
        print(priority)
        temp_dict_to_add = {'text': todo_text, 'priority': priority}
        todo_list.append(temp_dict_to_add)
        db.set('todos', todo_list)
        db.save()
        db.clear()
        
    return render_template('index.html', todo_list=todo_list)

app.run(debug=True)



######################################

# # Get a todo from the database.
# todo_list = db.get('todos')

# print(todo_list)

# # i is each todo in the list. WE are printing the priority.
# for i in range(len(todo_list)):
#     print(todo_list[i]['priority'])










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