from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    posts = [
        {
            'title': "The Lazy Way To Boy",
            'author': "Kevin Sage",
            'date': "October 4th, 2020",
            'body': "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
        }, 
        {
            'title': "Why Magic Is The Only Skill You Really Need",
            'author': "Wanda Chang",
            'date': "February 14th, 2021",
            'body': "Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem."

        },
        {
            'title': "Bullets And The Chuck Norris Effect",
            'author': "Fancy Name",
            'date': "July 24th, 2021",
            'body': "Windows NT addresses 2 Gigabytes of RAM, which is more than any application will ever need. (Microsoft, on the development of Windows NT, 1992) Programming is like sex: one mistake and you’re providing support for a lifetime. (Michael Sinz) I’ve noticed lately that the paranoid fear of computers becoming intelligent and taking over the world has almost entirely disappeared from the common culture. Near as I can tell, this coincides with the release of MS-DOS. (Larry DeLuca) The best performance improvement is the transition from the nonworking state to the working state."

        },
        {
            'title': "At Last, The Secret To Childhood Is Revealed",
            'author': "Donald James",
            'date': "December 20th, 2021",
            'body': "First, solve the problem. Then, write the code. (John Johnson) Programmers are in a race with the Universe to create bigger and better idiot-proof programs, while the Universe is trying to create bigger and better idiots. So far the Universe is winning. (Rich Cook) Most software today is very much like an Egyptian pyramid with millions of bricks piled on top of each other, with no structural integrity, but just done by brute force and thousands of slaves. (Alan Kay) The trouble with programmers is that you can never tell what a programmer is doing until it’s too late."

        },
    ]
    
    return render_template('lab3.html', posts = posts)

app.run(debug=True)