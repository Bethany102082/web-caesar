from flask import Flask, request
from caesar import encrypt

app = Flask(__name__)
app.config['DEBUG'] = True
form = """ <!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
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
      <!-- create your form here -->
        <form method="post">
        <label for="rot">Rotate by:</label>
        <input id="rot" type="text" name="rot" value="0">
        <br>
        <textarea rows="5" cols="55" name="text">{0}</textarea>
        <input type="submit">
</form> 
    </body>
</html>
"""
@app.route("/")
def index():
    return form.format("")

@app.route("/", methods=["POST"])
def encrypted():
    rot = int(request.form["rot"])
    text = encrypt(request.form["text"], rot)
    return form.format(text)

#form.format()

app.run()