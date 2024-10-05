from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def prva_strana():
    return render_template('index.html')

