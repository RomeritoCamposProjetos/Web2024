from flask import Blueprint, render_template, \
    request, url_for, redirect
from users.models import User
from books.models import Book
from emprestimo.models import Emprestimo

bp = Blueprint('emprestimo', 
    __name__, 
    url_prefix='/emprestimo', 
    template_folder='templates')

@bp.route('/')
def index():
    return render_template('emprestimo/index.html', 
        emprestimos = Emprestimo.all())

@bp.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        data = request.form['data']
        user = request.form['user']
        book = request.form['book']

        emprestimo = Emprestimo(data, user, book)
        emprestimo.save()
        return redirect(url_for('emprestimo.index'))
        

    return render_template('emprestimo/register.html', 
        users = User.all(),
        books = Book.all())