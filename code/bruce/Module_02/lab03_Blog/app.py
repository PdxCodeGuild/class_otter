# ********************************************************* #
#                        Lab 3: Blog                        #
#   flask responsive flexbox grid blog framework html css   #
#                        Version: 1.0                       #
#                    Author: Bruce Stull                    #
#                         2022-02-07                        #
# ********************************************************* #

# Assignment:
# https://github.com/PdxCodeGuild/class_otter/blob/bruce/2%20Flask%20+%20HTML%20+%20CSS/labs/03%20Blog.md

# Run Flask app:
# python app.py

from flask import Flask, render_template
import blog

# Test access to blog.posts:
print(f"Number of blog posts: {len(blog.posts)}")

posts = blog.posts

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', posts=posts)

# # @app.route('/author/<string:author>/')
# @app.route('/author/')
# def author():
#     posts = [post for post in blog.posts if post['author'] == 'GnomeChompsky']
#     return render_template('index.html', posts=posts)




app.run(debug=True)