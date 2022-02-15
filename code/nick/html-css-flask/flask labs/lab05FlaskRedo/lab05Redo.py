from flask import Flask, render_template, request, redirect
app = Flask(__name__)

metrics ={'ft': 0.3048, 'in': .9144, 'yd': .0254, 'mi': 1609.34, 'm': 1, 'km': 1000}

output = {}
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_distance = float(request.form['number'])
        unit = request.form['unit']
        conversion= user_distance * metrics[unit]
        output[unit] = conversion
        return redirect('/')
    return render_template('index.html',output=output,metrics=metrics)

app.run(debug=True)