from flask import Flask, render_template, request, redirect

app = Flask(__name__)

def encrypt(word, rotation=0):
    
    letters = ''
    for i in range(97, 123):
        letters += (chr(i))    

    rot_letters = letters[rotation:] + letters[:rotation]   

    new_word = ''
    for n in word:
        position = letters.find(n)
        new_word += rot_letters[position]
    
    return new_word

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        word = request.form['word']
        rotation = request.form['rotation']
        new_word = encrypt(word, int(rotation))
        return render_template('lab05.html', new_word=new_word)

    else:
        return render_template('lab05.html', new_word='')

app.run(debug=True)