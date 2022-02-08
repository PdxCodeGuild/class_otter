# ********************************************************* #
#                        Lab 2: Blog                        #
#   flask responsive flexbox grid blog framework html css   #
#                        Version: 1.0                       #
#                    Author: Bruce Stull                    #
#                         2022-02-07                        #
# ********************************************************* #

from flask import Flask, render_template
import blog

# Test access to blog.posts:
print(f"Number of blog posts: {len(blog.posts)}")

posts = blog.posts

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', posts=posts)



app.run(debug=True)