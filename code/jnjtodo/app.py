from typing import Text
from flask import Flask, render_template, request, redirect
from flask import request
from jsondb import JsonDB
import json
db = JsonDB()
db.load()

app = Flask(__name__)


# x = db.get('x', 0)
# x += 1
# db.set('x', x)
# db.save()

# @app.route('/')
# def index():
#     return render_template('index.html', todos=db['todos'])


@app.route('/', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        data = db.get('todos')
        data.append({
            'text': request.form['text'],
            'priority': request.form['priority']})
        db.save()
        return redirect('/')
    data = db.get('todos')
    return render_template('index.html', data=data)


app.run(debug=True)
