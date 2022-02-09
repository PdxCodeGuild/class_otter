# Flask Todo List
# Mob 4
# Group 2
# Sana Rahmani, Justin Hammond, Jacob McElhaney, and Keenan Tabusa


# Let's build a todo list with Flask and a simple database that uses JSON to store the data.

# Part 1
# Create a folder for your lab, and inside of that create a db.json with the following contents:

# db.json

# {
#   "todos":[
#     {
#       "text": "walk the dog",
#       "priority": "high"
#     },{
#       "text":"butter the cat",
#       "priority":"medium"
#     },{
#       "text":"wash dishes",
#       "priority":"low"
#     }
#   ]
# }
# Next, write a Flask app that uses the JsonDB class to load the database and render a template containing the information. The resulting HTML should look something like this, but feel free to use a table or divs instead.

# <ul>
#   <li>walk the dog (high)</li>
#   <li>butter the cat (medium)</li>
#   <li>wash dishes (low)</li>
# </ul>

# Part 2
# Using a form, allow the user to save a new todo item to the database. This should include a input for text, a select for the priority, and a button for submitting the form.

<<<<<<< HEAD

# import jsondb
from jsondb import JsonDB
=======
from jsondb import JsonDB 
>>>>>>> b36e2449f1b32062f00d23b84eaab90c4f18795c
db = JsonDB('db.json')
db.load()
x = db.get('x', 0)
x += 1
db.set('x', x)
db.save()
from flask import Flask, render_template , request, redirect
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        contact_name = request.form['input_text']
        print(contact_name)
        # handle data here
        return redirect('/')
    return render_template('index.html')