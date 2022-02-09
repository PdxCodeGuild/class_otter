# Import JsonDB 'class' from jsondb 'module'.
from jsondb import JsonDB

# Import some stuff from flask.
from flask import Flask, render_template, request, redirect

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
        # 
        contact_name = request.form['input_text']
        print(contact_name)

    return render_template('index.html', todo_list=todo_list)



app.run(debug=True)




######################################

# # Get a todo from the database.
# todo_list = db.get('todos')

# print(todo_list)

# # i is each todo in the list. WE are printing the priority.
# for i in range(len(todo_list)):
#     print(todo_list[i]['priority'])