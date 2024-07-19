from flask import Flask, make_response, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('cookies.html')


# definindo cookies de sessão
# aqui ele expira quando o navegador for encerrado
@app.route("/cookie1")
def cookie1():
    text = "<h1>Um cookie foi definido<h1/>"
    response = make_response(text)
    response.set_cookie('session_cookie', 'teste')
    return response

# aqui a rota só recebe request POST
# obtemos o tempo enviado em segundos(não validamos)
# esse tempo será usado para definir o tempo de vida do cookie
# este cookie é um cookie permanente
# o atributo max_age determina o tempo de vida dele
# mesmo fechando o navegador, não será apagado
@app.route("/cookie2", methods=['POST'])
def cookie2():
    text = "<h1>Um cookie foi definido<h1/>"
    time = int(request.form['time'])
    response = make_response(text)
    response.set_cookie('permanent_cookie', 'teste', max_age=time)
    return response


@app.route("/cookie3", methods=['POST'])
def cookie3():
    option = eval(request.form['opcao'])
    template = render_template('httponly.html', opcao=str(bool(option)), dado='red')
    response = make_response(template)
    if 'http_only' in request.cookies:
        response.delete_cookie(request.cookies['http_only'])
    response.set_cookie('http_only', str(bool(option)), httponly=bool(option))
    return response


