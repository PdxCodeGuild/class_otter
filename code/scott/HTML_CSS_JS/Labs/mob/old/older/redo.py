from logging import debug
# from flask import Flask, render_template, request, redirect
import random
import string
letters = string.ascii_letters
digits = string.digits
punctuation = string.punctuation
# password = []

app = Flask(__name__)

@app.route('/')
def index():
    
    return render_template('index.html')
# redo = Flask(__name__)


@app.route('/password', methods=["POST"])
def password():
            
    pwl = int(request.form["please enter a Password length between 8 and 16:"])
    ucl = int(request.form["How many characters should be Uppercase? (A -Z):"])
    lcl = int(request.form["How many characters should be Lowercase? (a-z):"])
    nums = int(request.form["How many characters should be numbers? (0 - 9)?:"])
    punc = int(request.form["How many Punctuation Characters should be used?:"])
    
    # numbers = int(request.form['how-many1'])
    # letters = int(request.form['how-many2'])
    # user_punctuation = int(request.form['how-many3'])

    ascii_letters_up = string.ascii_letters.upper
    ascii_letters_low = string.ascii_letters.lower
    digits = string.digits
    punctuation = string.punctuation

    possibile_letters_up = ascii_letters_up
    possibile_letters_low = ascii_letters_low
    possible_numbers = digits
    possible_punctuation_numbers = punctuation

    pw_ucl_num = ""
    pw_lcl_num = ""
    pw_num_num = ""
    pw_punc_num = ""
    
    w = 0
    x = 0
    y = 0
    z = 0
    
    pwl_num = 0
    while pwl_num <= int(pwl):
        if w <= int(ucl):
            pw_ucl_num += random.choice(possibile_letters_up)
            w += 1
            pwl_num += 1
        elif x <= int(lcl):
            pw_lcl_num += random.choice(possibile_letters_low)
            x += 1
        elif y <= int(nums):
            pw_num_num += random.choice(possible_numbers )
            y += 1
        elif z <= int(punc):
            pw_punc_num += random.choice(possible_punctuation_numbers)
            z += 1
        else:
            return 

    user_password = str(pw_ucl_num + pw_lcl_num + pw_num_num + pw_punc_num) 

    final_password = list(user_password) 

    random.shuffle(final_password)
    print(final_password)
    
    return render_template('password.html', final_password=final_password)



app.run(debug=True)

# while len(password) < 10:
#     #add a random character to the list
#     password.append(random.choice(all_characters))
# def listToString(password):
#     str1 = ""
#     return (str1.join(password))
# print("\nHere is your Random Password:\n")
# print(listToString(password))

