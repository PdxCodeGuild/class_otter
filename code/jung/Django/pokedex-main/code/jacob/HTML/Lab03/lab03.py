from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    blogs = [
        {'title': "Der Hast", 'author': "Jay", 'date': "January 4th, 2022", 'body': "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."},
        {'title': "Monaker", 'author': "Susan", 'date': "December 20th, 2021", 'body': "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."},
        {'title': "Where you gotta be", 'author': "Jessie", 'date': "November 1st, 2021", 'body': "Tellus in metus vulputate eu scelerisque felis imperdiet proin. Id consectetur purus ut faucibus pulvinar elementum. Quam id leo in vitae. Dolor purus non enim praesent elementum facilisis leo vel fringilla. Mauris pharetra et ultrices neque ornare aenean euismod."},
        {'title': "Let's go people", 'author': "Brad", 'date': "July 5th, 2021", 'body': "Etiam sit amet nisl purus in mollis nunc sed id. Odio tempor orci dapibus ultrices in. Praesent elementum facilisis leo vel fringilla est. Egestas maecenas pharetra convallis posuere morbi leo. Proin libero nunc consequat interdum."}
    ]
    return render_template('lab03.html',blogs=blogs)



app.run(debug=True)