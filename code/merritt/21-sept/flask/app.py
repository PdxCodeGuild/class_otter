from flask import Flask, render_template
app = Flask(__name__)

who_is_cool = "Calen"
temperature = 212
shopping_list = ['milk', 'eggs', 'bread', 'ALSO BUTTER']

@app.route('/')
def index():
    return render_template('index.html', who_is_cool=who_is_cool, temperature=temperature, shopping_list=shopping_list)

app.run(debug=True)