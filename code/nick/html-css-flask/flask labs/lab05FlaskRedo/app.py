from flask import Flask, render_template, request, redirect
app = Flask(__name__, static_folder='static')

metrics ={'ft': 0.3048, 'in': .9144, 'yd': .0254, 'mi': 1609.34, 'm': 1, 'km': 1000}
output = [1]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_distance = float(request.form['number'])
        unit = request.form['unit']
        conversion = user_distance * metrics[unit]
        output[0]=conversion
        return redirect('/')
    return render_template('index.html', output=output)

if __name__ == '__main__':
    app.run(debug=True)