from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        text = request.form["text"].lower()
        cipher = request.form["cipher"]
        rotate = request.form["rotate"]
        ask_list = [i for i in text]
        # print(ask_list)


        #make a list of index contains 0 - 25
        index = []
        for num in range(0,26):
            index.append(num)
        # print(index)

        #make a list of english contains a - z
        english = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        # print(english)

        #iterate through the index list and 
        rot = []

        for letter in ask_list:
            letter_num = english.index(letter)
            if cipher == "encryption":
                letter_num += int(rotate)
                rot.append(english[letter_num])
            elif cipher == "decryption":
                letter_num -= int(rotate)
                rot.append(english[letter_num])
        print(rot)

        rot = ''.join(rot)
        return render_template('lab5.html', data = rot)


    return render_template('lab5.html', data = None)
app.run(debug=True)




    

            