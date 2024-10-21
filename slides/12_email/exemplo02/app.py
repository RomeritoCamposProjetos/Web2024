from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.postmarkapp.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USERNAME'] = 'romerito.campos@escolar.ifrn.edu.br'
app.config['MAIL_PASSWORD'] = 'adbfdc7d-75c2-4709-89f8-f932cdf4c356'
app.config['POSTMARK_HEADER'] = {'X-PM-Message-Stream':'teste'}

mail = Mail(app)

@app.route('/')
def send():    
    msg = Message('teste', sender='romerito.campos@escolar.ifrn.edu.br',
                  recipients=['romerito.campos@escolar.ifrn.edu.br'],
                  extra_headers=app.config['POSTMARK_HEADER'])
    
    msg.body = 'teste'
    msg.html = 'this is is '
    with app.app_context():
        mail.send(msg)
        
    return "teste"