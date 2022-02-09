from jsondb import JsonDB
db = JsonDB('db.json')
db.load()
from flask import Flask, render_template, request, redirect
app = Flask(__name__)


# x = db.get('todos', 0)
# x += 1
# db.set('todos', x)
# db.save()


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        contact_name = request.form['input_text']
        print(contact_name)
        # handle data here
        return redirect('/')
    return render_template('index.html')