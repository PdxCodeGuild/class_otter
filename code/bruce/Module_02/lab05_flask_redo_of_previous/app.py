# ********************************************** #
#       Lab 5: Flask Redo - Unit Converter       #
#   flask request http html css unit converter   #
#                  Version: 1.0                  #
#              Author: Bruce Stull               #
#                   2022-02-10                   #
# ********************************************** #


# Import some stuff from flask.
from flask import Flask, render_template, request
# 'conversion' is a dictionary of 'unit':'conversion-factor' pairs.
# 'length_converter' is a function with converts the length.
from unit_converter import conversion, length_converter


# Assignment:
# https://github.com/PdxCodeGuild/class_otter/blob/main/2%20Flask%20%2B%20HTML%20%2B%20CSS/labs/05%20Flask%20Redo.md

# Resources:

# Length converter:
# https://github.com/PdxCodeGuild/Programming102/blob/master/labs/lab3.md

# My length converter solution:
# https://github.com/brucestull/pdx_code_102/blob/main/labs/unit_3/lab_03_Extra.py

# Flask and HTML:
# HTML Forms: https://github.com/PdxCodeGuild/class_otter/blob/bruce/2%20Flask%20%2B%20HTML%20%2B%20CSS/docs/11%20HTML%20Forms.md
# Flask: https://github.com/PdxCodeGuild/class_otter/blob/bruce/2%20Flask%20%2B%20HTML%20%2B%20CSS/docs/12%20Flask.md
# Flask Forms: https://github.com/PdxCodeGuild/class_otter/blob/bruce/2%20Flask%20%2B%20HTML%20%2B%20CSS/docs/13%20Flask%20Forms.md


# Create Flask object, we're going to call it 'app'.
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the user input values from Flask request.form['key']:
        input_unit = request.form["input-unit"]
        output_unit = request.form["output-unit"]
        input_length = request.form["input-length"]

        # print(f"input_length: {input_length}")
        # print(f"input_unit: {input_unit}")
        
        # Creat a dictionary of the input length and input units:
        input_values = {'length': input_length, 'units': input_unit}

        # Calculate the output length:
        output_length = round(
            length_converter(
                float(input_length),
                input_unit,
                output_unit,
                conversion),
                3)
        
        # Create a dictionary of the output length and output units:
        output_values = {'length': output_length, 'units': output_unit}

        # Return data via 'render_template('index.html', data=data)'
        return render_template('index.html',
            input_values=input_values,
            output_values=output_values,
            conversion=conversion)
    
    # Only need the dictionary 'conversion' upon initial load of page.
    # This will provide the units to populate the unit choice box.
    return render_template('index.html', conversion=conversion)


app.run(debug=True)
