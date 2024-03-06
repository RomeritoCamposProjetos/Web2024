from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    name = request.args.get('name')
    return render_template('profile.html', name=name)