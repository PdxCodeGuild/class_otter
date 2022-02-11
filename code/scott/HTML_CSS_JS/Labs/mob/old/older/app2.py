#redoing the password generator lab with flask and html/css

from flask import Flask, app, render_template, request, url_for
from random import choice,shuffle
from string import ascii_lowercase,ascii_uppercase,digits,punctuation
app = Flask(__name__)


def make_pass(upper,lower,punct,nums):
    new_pass = []

    total = upper + lower + punct + nums
    if total > 10:
        return "Password cannot exceed 10 characters"
    check = 0

    while check != total:
        if check < upper:
            new_pass.append(choice(list(ascii_uppercase)))
            check += 1
        elif check < upper + lower:
            new_pass.append(choice(list(ascii_lowercase)))
            check += 1
        elif check < upper + lower + punct:
            new_pass.append(choice(list(punctuation)))
            check += 1
        elif check < total:
            new_pass.append(choice(list(digits)))
            check += 1
    shuffle(new_pass)
    new_pass = ''.join(new_pass)
    return new_pass

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        password = make_pass(int(request.form['uppercase']),int(request.form['lowercase']),int(request.form['punctuation']),int(request.form['numbers']))
        return render_template('index.html', password=password)

app.run(debug=True)