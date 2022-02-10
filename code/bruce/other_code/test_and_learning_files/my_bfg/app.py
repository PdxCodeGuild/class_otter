# Assignment:
# https://github.com/PdxCodeGuild/class_otter/blob/main/2%20Flask%20%2B%20HTML%20%2B%20CSS/mob/04%20Flask%20Todo%20List.md

# Resources:

# My repository:
# https://github.com/PdxCodeGuild/class_otter/tree/bruce/code/bruce/other_code/test_and_learning_files/my_bfg

# Flask forms:
    # https://github.com/PdxCodeGuild/class_otter/blob/main/2%20Flask%20+%20HTML%20+%20CSS/docs/13%20Flask%20Forms.md

# HTML forms:
    # https://github.com/PdxCodeGuild/class_otter/blob/main/2%20Flask%20+%20HTML%20+%20CSS/docs/11%20HTML%20Forms.md

# jsondb.py:
    # https://github.com/PdxCodeGuild/class_otter/blob/main/2%20Flask%20+%20HTML%20+%20CSS/mob/jsondb.py



# Import JsonDB 'class' from jsondb 'module'.
from jsondb import JsonDB

# Import some stuff from flask.
from flask import Flask, render_template, request, redirect

# Create Flask object.
app = Flask(__name__)

# Should this be in function or not?
# Create JsonDB object.
db = JsonDB('db.json')
db.load()


@app.route('/', methods=['GET', 'POST'])
def index():
    
    ######## !!! I think this should be in the function. !!! ########
    # Get the todos from the database.
    todo_list = db.get('todos')
    print(f"todo_list: {todo_list}")
    #################################################################
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


####################################
# Josse group's solution:
# @app.route('/', methods=['GET', 'POST'])
# def create():
#     if request.method == 'POST':
#         data = db.get('todos')
#         data.append({
#             'text': request.form['text'],
#             'priority': request.form['priority']})
#         db.save()
#         return redirect('/')
#     data = db.get('todos')
#     return render_template('index.html', data=data)
####################################



app.run(debug=True)


