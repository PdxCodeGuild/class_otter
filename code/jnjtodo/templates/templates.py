from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    {
    "todos":[
      {
        "text": "walk the dog",
        "priority": "high"
      },{
        "text":"butter the cat",
        "priority":"medium"
      },{
        "text":"wash dishes",
        "priority":"low"
      }
    ]
  }
    return render_template('index.html', todos = todos)

app.run(debug=True)