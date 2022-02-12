
from flask import Flask, render_template, request
app = Flask(__name__)

english = {"a": "n", "b": "o", "c": "p", "d": "q", "e": "r", "f": "s", "g": "t", "h": "u", "i": "v", "j": "w", "k": "x", "l": "y", "m": "z",
           "n": "a", "o": "b", "p": "c", "q": "d", "r": "e", "s": "f", "t": "g", "u": "h", "v": "i", "w": "j", "x": "k", "y": "l", "z": "m"}


def encrypt(word, dict):
    '''WORD is the word to be encrypted or decrypted. ENCRYPTION_DICTIONARY is the ROT-13 dictionary used for encryption-decryption.'''
    working_list = []
    for character in word:
        working_list.append(dict[character])
    the_final_word = ''.join(working_list)
    return the_final_word


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['input_text']
        print(user_input)
        rot_word = encrypt(user_input, english)
        print(rot_word)

        return render_template('index.html', rot_word=rot_word)
    return render_template("index.html")


app.run(debug=True)
