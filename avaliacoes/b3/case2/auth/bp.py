from flask import Blueprint, request, redirect, url_for, render_template
from flask_login import logout_user, login_user, LoginManager, login_required
from models.user import User

# definir login_manager
login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    return User.find(id=user_id)

# criar bluprint de auth
auth_bp = Blueprint(
    name='auth', 
    import_name=__name__,
    url_prefix='/auth',
    template_folder='templates')

# definir rota para login
@auth_bp.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        user = User.find(email=email)
        if user:
            login_user(user)
            return redirect(url_for('users.index'))
    return render_template('auth/login.html')

#definir rota para logout
# logout apenas com usuários logados
# apenas método post
@auth_bp.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))



