from flask import Flask, request
from markupsafe import escape
app = Flask(__name__)

@app.route('/')
def index():
    name= request.args.get('name')
    print(request)
    print (request.url)
    print(request.method)    
    return f'<h1>Hello World, {escape(name)}</h1>'