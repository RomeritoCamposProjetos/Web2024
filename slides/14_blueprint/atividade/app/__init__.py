from flask import Flask, render_template
from users import users
from books import books
from emprestimo import emprestimo

app = Flask (__name__, template_folder='templates')

app.register_blueprint(users.bp)
app.register_blueprint(books.bp)
app.register_blueprint(emprestimo.bp)

@app.route('/')
def index():
    return render_template('layout.html')