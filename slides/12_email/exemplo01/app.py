from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'romerito.campos@escolar.ifrn.edu.br'
app.config['MAIL_PASSWORD'] = 'feppfbaturghimrc'

mail = Mail(app)

@app.route('/')
def send():
    msg = Message('teste', sender='romerito.campos@escolar.ifrn.edu.br',
                  recipients=['romerito.campos@escolar.ifrn.edu.br'])
    
    msg.body = 'teste'
    msg.html = 'this is is '
    with app.app_context():
        mail.send(msg)
        
    return "teste"

