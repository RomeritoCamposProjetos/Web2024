from werkzeug.security import check_password_hash, generate_password_hash

class User:
    def __init__(self, **kwargs):
        self._id = None
        if 'email' in kwargs.keys():
            self._email = kwargs['email']
        if 'password' in kwargs.keys():
            self._password = kwargs['password']
        if 'hash' in kwargs.keys():
            self._hash = kwargs['hash']
        else:
            self._hash = generate_password_hash(self._password)


user = User(email='12@12', password='12')
print(check_password_hash(user._hash, '12'))