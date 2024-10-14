# $env:FLASK_APP = "static.py"
# $env:FLASK_DEBUG = 1
# flask run
# py -m flask run
# http://127.0.0.1:5000/

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def prva_strana():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)