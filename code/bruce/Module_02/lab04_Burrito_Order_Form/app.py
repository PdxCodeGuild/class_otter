# ******************************************** #
#          Lab 4: Burrito Order Form           #
#   flask html form css index selector input   #
#                 Version: 1.0                 #
#             Author: Bruce Stull              #
#                  2022-02-08                  #
# ******************************************** #

from flask import Flask, render_template
from customer_info import customer
from menu_info import *
# from menu_info import menu_wrap as menu_wrap
# from menu_info import menu_rice as menu_rice
# from menu_info import menu_beans as menu_beans
# from menu_info import menu_protein as menu_protein
# from menu_info import menu_add as menu_add



# Assignment:
# https://github.com/PdxCodeGuild/class_otter/blob/bruce/2%20Flask%20%2B%20HTML%20%2B%20CSS/labs/04%20Burrito%20Order%20Form.md

# Activate virtual environment (in BASH):
# source C:/Users/Bruce/.virtualenvs/lab04_Burrito_Order_Form-b4iS58LK/Scripts/activate

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', customer=customer, menu_wrap=menu_wrap, menu_rice=menu_rice, menu_beans=menu_beans, menu_protein=menu_protein, menu_add=menu_add)





app.run(debug=True)