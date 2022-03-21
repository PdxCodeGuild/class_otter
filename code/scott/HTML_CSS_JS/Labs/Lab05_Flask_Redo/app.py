#redoing the password generator lab with flask and html/css

from itertools import count
from flask import Flask, app, render_template, request, url_for
from random import choice,shuffle
from string import ascii_lowercase,ascii_uppercase,digits,punctuation
app = Flask(__name__)


def make_pass(upper,lower,punct,nums):#define Function
    new_pass = [] #Create mpty LList

    total = upper + lower + punct + nums #(Add) number selected of each Character Types.
    if total > 16: # decision point
        return "Password cannot exceed 16 characters"
    count = 0 #variable to compare against 'total'

    while count != total: #build new_pass loop
        if count < upper: #Decision Point for Upper Character loop
            new_pass.append(choice(list(ascii_uppercase)))
            count += 1
        elif count < upper + lower: #Decision Point for Lower Character loop
            new_pass.append(choice(list(ascii_lowercase)))
            count += 1
        elif count < upper + lower + punct: #Decision Point for Special Character loop
            new_pass.append(choice(list(punctuation)))
            count += 1
        elif count < total: #Decision Point for Number Character loop
            new_pass.append(choice(list(digits)))
            count += 1
    shuffle(new_pass) # Randomly Shuffle final 'new_pass' characters
    new_pass = ''.join(new_pass) #concatinate strings into one string "new_pass"
    return new_pass

@app.route('/', methods=['GET', 'POST']) #set up route and 
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        password = make_pass(int(request.form['uppercase']),int(request.form['lowercase']),int(request.form['punctuation']),int(request.form['numbers']))
        return render_template('index.html', password=password)

app.run(debug=True)