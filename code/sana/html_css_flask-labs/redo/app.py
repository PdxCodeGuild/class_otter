from flask import Flask, render_template, request
app = Flask(__name__)
import random
import string

@app.route('/', methods=['GET', 'POST'])
def index():
    print(request.method)

    if request.method == 'POST':
        length = request.form['Blank']
        length = int(length)
        letters = string.ascii_letters
        digits = string.digits
        punc = string.punctuation
        all_chars = letters + digits + punc
        i = 0
        password_char = []
        while i <= length:
            i += 1
            chosen_chars = random.choice(all_chars)
            chosen_chars = str(chosen_chars)
            password_char.append(f'{chosen_chars}')
            password = ("You password is: " + ''.join(password_char))

        return render_template('index.html', password=password)
    else:
        return render_template('index.html', password='')


app.run(debug=True)