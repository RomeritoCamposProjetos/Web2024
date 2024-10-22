from flask import Flask, render_template, url_for, request, Blueprint

bp = Blueprint('books', __name__, url_prefix='/books', template_folder='templates')

@bp.route('/')
def index():
    return render_template('books/index.html')