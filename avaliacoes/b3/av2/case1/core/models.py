from flask_login import UserMixin

class User(UserMixin):
    id:int = 1    
    def get_id(self):
        return 1