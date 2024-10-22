from flask import Flask, render_template
from users import user

app = Flask (__name__, template_folder='templates')

app.register_blueprint(user.bp)

@app.route('/')
def index():
    return render_template('layout.html')