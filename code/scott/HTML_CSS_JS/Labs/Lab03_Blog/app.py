from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    blogs = [
        {
            'title': "Der Hast",
            'author': "Kirkegaurd", 
            'date': "May 4th, 1880", 
            'body': "ipsum vulputate eu leo vel fringilla est."
            },
        {
            'title': "Der Downer", 
            'author': "Neitzche", 
            'date': "October 16th, 1872", 
            'body': "Convallis posuere morbi leo illum dolore eu fugiat. Excepteur in culpa qui elementum."
             },
        {
            'title': "Ein Dunder", 
            'author': "Sartre", 
            'date': "March 1st, 1921", 
            'body': "Consectetur purus putate il maecenas  fisqueis imperdiet faucibus."
            },
        {
            'title': "Puba Grande", 
            'author': "Heideger", 
            'date': "June 10th, 1680", 
            'body': "Morbi est intelligentsia hella vidi vici veni allure."
            }
    ]
    return render_template('index.html',blogs=blogs)

app.run(debug=True)