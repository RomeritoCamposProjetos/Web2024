from flask import render_template, redirect, url_for, request, flash
from case2 import app
from case2.models.user import User

@app.route('/users')
def index():    
    return render_template('users/index.html', users=User.all())

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        nome= request.form['nome']

        if not email:
            flash('Email é obrigatório')
        else:
            user = User(email, nome)
            user.save()
            return redirect(url_for('index'))
    
    return render_template('users/register.html')

