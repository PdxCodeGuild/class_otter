from jsondb import JsonDB
db = JsonDB()
db.load()

from flask import request
from flask import Flask, render_template, request, redirect
app = Flask(__name__)


# x = db.get('x', 0)
# x += 1
# db.set('x', x)
# db.save()

@app.route('/')
def index():
    return render_template('index.html', todos=db['todos'])



@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        db['todos'].append({
            'text': request.form['text'],
            'priority'
        })
        return redirect('/')
    return render_template('index.html')