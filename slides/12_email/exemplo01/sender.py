from smtplib import SMTP
from dotenv import load_dotenv
import os

# vai carregar os dados do arquivo .env do projeto
# definir variáveis de ambiente
load_dotenv()

message = f"""\
Subject: Ola
To: {os.getenv('SENDER')}
From: {os.getenv('SENDER')}

Alguma coisa escrita aqui."""


with SMTP(host=os.getenv('SMTP_SERVER'), port=os.getenv('PORT')) as server:
    server.starttls()
    server.login(os.getenv('SENDER'), os.getenv('PASSWORD'))
    server.sendmail(os.getenv('SENDER'), os.getenv('SENDER'), msg=message)




