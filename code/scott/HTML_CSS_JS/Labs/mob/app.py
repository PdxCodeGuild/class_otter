
# Import some stuff from flask.
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

