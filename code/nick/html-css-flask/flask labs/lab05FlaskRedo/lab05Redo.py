import re
from flask import Flask, render_template, request, redirect
app = Flask(__name__)

metrics = [
    {
        'ft': 0.3048
    },
    {
       'in': 1609.34
    },
    {
        'mi': 1609.34
    },
    {
        'm': 1
    },
    {
        'km': 1000
    },
    {
        'yd': 0.9144
    },
    {
        'in' : .0254
    }
    ]
data = []
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        request.form['number'] * metrics['Units']
        return redirect('/')
    return render_template('index.html', data=data,metrics=metrics)

app.run(debug=True)