from flask import Flask, request, render_template, redirect
from rotation_cipher import RotationCipher


app = Flask(__name__)
max_rotation = RotationCipher.allowed_characters_size

@app.route('/')
def index():
    if len(request.args) > 0:
        encoded_message = request.args['encoded_message']
        if encoded_message is not None:
            return render_template('index.html', should_hide='', encoded_message=encoded_message, max_rotation=max_rotation)
    else:
        return render_template('index.html', should_hide='hide', encoded_message='', max_rotation=max_rotation)

@app.route('/encode/', methods=['POST'])
def encode():
    encoded_message = RotationCipher.encrypt(request.form['message'], int(request.form['rotation_value']))
    return redirect(f'/?encoded_message={encoded_message}')





if __name__ == "__main__":
    app.run(debug=True)