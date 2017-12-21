

from flask import Flask, request
import string
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True
form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font:16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>

        <form action="/" method="post">
            <label for="fot">
                rotate by:

                <input type="text" id="rot" name="rot" value="0">
                    <textarea id="text" name="text">{0}
                    </textarea>
                </input
            </label>

            <input type="submit" value="Submit query">
            </input>
        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form.format('')

@app.route("/", methods=['POST'])
def encrypt():
    my_rot = int(request.form['rot'])
    my_text= request.form['text']

    encrypted_text = rotate_string(my_text,my_rot)
    return form.format(encrypted_text)

app.run()
