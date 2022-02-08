# ******************************************** #
#          Lab 4: Burrito Order Form           #
#   flask html form css index selector input   #
#                 Version: 1.0                 #
#             Author: Bruce Stull              #
#                  2022-02-08                  #
# ******************************************** #

from flask import Flask, render_template

# Assignment:
# https://github.com/PdxCodeGuild/class_otter/blob/bruce/2%20Flask%20%2B%20HTML%20%2B%20CSS/labs/04%20Burrito%20Order%20Form.md

# Activate virtual environment (in BASH):
# source C:/Users/Bruce/.virtualenvs/lab04_Burrito_Order_Form-b4iS58LK/Scripts/activate

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')





app.run(debug=True)