from flask import Flask
from users import user

app = Flask (__name__)
app.register_blueprint(user.bp)

@app.route('/')
def index():
    return "Testando blueprints"