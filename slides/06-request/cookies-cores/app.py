from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/color', methods=['POST', 'GET'])
def color():
    cor = request.form['color']
    template = render_template('color.html', cor=cor)
    response = make_response(template)
    if 'color' in request.cookies and cor != request.cookies['color']:    
        response.delete_cookie('color')
    response.set_cookie('color', cor)
    return response
    
    