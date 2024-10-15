from flask import Flask, render_template
from dotenv import load_dotenv
from flask_mail import Mail, Message
import os

load_dotenv()

mail = Mail()

app = Flask(__name__)
app.config['MAIL_SERVER'] = os.getenv('SERVER')
app.config['MAIL_PORT'] = os.getenv('PORT')
app.config['MAIL_USERNAME'] = os.getenv('SENDER') 
app.config['MAIL_PASSWORD'] = os.getenv('PASSWORD')
app.config['MAIL_USE_TLS'] = os.getenv('TLS')
# app.config['MAIL_USE_SSL'] = os.getenv('SSL')

mail.init_app(app)

@app.route('/')
def index():
    msg = Message(
        'Hello',
        recipients=['romerito.campos@escolar.ifrn.edu.br'],
        body='this is an email',
        sender=os.getenv('SENDER')
    )
    mail.send(msg)
    return "Sucesso"

