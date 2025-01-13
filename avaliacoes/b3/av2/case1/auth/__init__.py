from flask_login import LoginManager
from core.models import User

login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    user = User()
    user.id = 1
    return user