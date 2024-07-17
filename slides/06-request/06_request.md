---
marp: true
theme: gaia
footer: Programação de Sistemas para Internet - Prof. Romerito Campos
_class: lead
size: 16:9
backgroundColor: #fff
style: |
    .linha {
        text-decoration: underline;
        color: blue;
    } 
    h2 {
        text-decoration: underline;
    }       
---

![w:120 h:120](../../assets/ifrn-vertical.png)
# Programação de Sistemas para Internet
Prof. Romerito Campos

---

# Plano de Aula

- Objetivo:
    - Compreender cookies e suas aplicações no desenvolvimento web

---

## Conteúdos

- Acessar dados da requisição
  - Objeto Request
  - Cookies
- Session

---

<style scoped>
    section {
        display: flex;
        flex-direction: column;
        justify-content: center;
        text-align: center;
    }
</style> 

# Objeto `request`

---

## Objeto request

- É necessário notar que precisamos ter interação entre cliente-servidor para usarmos o objeto `request`

- Portanto, consideraremos que já somos capazes de utilizar formulários HTML e também requisições com string de consulta (requisições GET)

---


## Objeto Request

- Use `request` para acessar dados do cliente

```python
from flask import request
```

- Atributos comuns:
  - `request.form`: Dados de formulário
  - `request.args`: Parâmetros de URL
  - `request.files`: Upload de arquivos
  - `request.values`: combina os dados de `form` e `args`

---

<style scoped>
    pre {
        float: left;
        width: 45%;
        margin-right: 5px;
        margin-top: 0px
    }
</style>

## Objeto request

- Formulário HTML

```html
<!-- trecho de código HTML -->
<form action="{{ url_for('form1') }}" method="POST">
    <input type="text" name="name">
    <input type="submit">
</form>
```

```python
# manipulando o form recebido
@app.route('/form1', methods=['POST', 'GET'])
def form1():
    if request.method == 'POST':
        name = request.form['name']    
        return "Você enviou o nome: " + name
    else:
        return redirect(url_for('formularios'))
``` 

---

## Objeto request

- No código anterior, temos o uso do atributo `methods` para indicar qual o tipo de métido suportado pela rota. 

- `methods` faz referência métodos HTTP como POST, GET entre outros.

- Para obtermos o método da requisição utilizamos `request.methods`

- Para obtermos os dados enviados via POST utilizamos `request.form[]`.
  - Devemos indicar o nome do input que no exemplo é `name` 


---

## Objeto request

<style scoped>
    pre {
        float: left;
        width: 45%;
        margin-right: 5px;
        margin-top: 0px
    }

    br {
        clear: both;
    }
</style>

- Envio de dados via HTTP GET utilizando string de consulta

```html
<h2>Envio de dados via GET para "form2"</h2>
<form action="{{ url_for('form2') }}" method="GET">
    <select name="opcao">
        <option value="red">Red</option>
        <option value="blue">Blue</option>
        <option value="green">Green</option>        
        <option value="yellow">Yello</option>        
    </select>
    <input type="submit" value="Enviar">
</form>
```

```python
@app.route('/form2', methods=['GET', 'POST'])
def form2():
    data = request.args.get('opcao')
    return data
```
<br />

- Aqui enviamos os dados via querystring, supondo a escolha de "red" temos: `http://localhost:5000/form2?opcao=red`.


---

## Objeto request

- Quando enviamos dados via GET como no exemplo das cores, podemos usar o atributo `request.args` do objeto `request` para obter os dados enviados.

- Neste caso, utilizamos o `name` que foi atribuído no HTML que no caso é `opcao` 
    
`request.args.get('opcao')`

---

<style scoped>
    section {
        display: flex;
        flex-direction: column;
        justify-content: center;
        text-align: center;
    }
</style> 

# Manipulação de Cookies


---

## Manipulação de Cookies

**O que são?**

- São pequenos pacotes de dados salvos como arquivos em nosso navegador que permitem uma melhor experiência na web e na comunicação com servidor

- Uma vez salvos no nosso navegador, podemos definir algumas propriedades do cookie que alteram seu comportamento

- Os cookies que são definidos em nosso navegador sempre vão junto nas próximas requisições

---

## Manipulação de Cookies

**Algumas aplicações:**

- Gerenciar sessão de usuários
- Melhorar experiência por meio de personalizações
- Rastreamento
    - comportamento do usuário
    - cliques realizados
    - localização

---

## Manipulação de Cookies

- Os cookies são armazenados no navegador na parte de **Storage**
    - No google chrome você pode abrir a DevTools (Ctrl + Shift C ou F12)
    - Ir até Application (aplicação)
    - Abrir o Storage e acessar os Cookies

- Veja a imagem no próximo slide

---

## Manipulção de Cookies


![width:1000px](./img/cookie.png)

---

## Manipulação de Cookies

**Como podemos manipular cookies em Flask?**

- Acesso: Através do atributo `cookie` do objeto `request` 

- Definição de cookies: através do uso de objetos `response` e a função `set_cookie`

- Vejamos um simples exemplo

---

## Manipulação de Cookies

- Vejamos como definir um cookie em Flask através de exemplos práticos

- Os arquivos do projeto estão na pasta cookies:
    - **app.py**: define as rotas que criam os cookies
    - **templates**: mostra o arquivo cookies.html que permite interagir com o projeto

---

## Manipulação de Cookies

- Exemplo 1
- Definição de cookie de sessão
- Este cookie expira quando o navegador é fechado
---

## Manipulação de Cookies

- Código da página `cookies.html`: Exemplo 1.

```html
<!-- trecho de código -->
<h4>Definido cookie de sessão</h4>
<a href="{{ url_for('cookie1') }}">Cookie de Sessão</a>
```

```python
# rota que manipula a criação de cookie
@app.route("/cookie1")
def cookie1():
    text = "<h1>Um cookie foi definido<h1/>"
    response = make_response(text)
    response.set_cookie('primeiro_cookie', 'teste')
    return response
```

---

## Manipulação de Cookies

- No exemplo anterior, temos uma nova função que é `make_response`

- Note que a interação cliente-servidor é feita através de `request-response`

- Você pode estar em dúvida se `return render_template` é um response. O flask vai produzir um response através deste retorno.

- Vamos criar manualmente o response para poder definir um cookie antes de dar a resposta ao usuário.

---

## Manipulação de Cookies

- Definição da string que será usada para retorno
`text = "<h1>Um cookie foi definido<h1/>"`
- Criação de um objeto `response` 
`response = make_response(text)`

- Uso da função set_cookie para enviar um cookie para o usuário
`response.set_cookie('primeiro_cookie', 'teste')`

- Aqui retorna-se um reponse(resposta) junto com o cookie que
`return response`

---

## Manipulação de Cookies

- Exemplo 2
- Criaremos um cookie permanente (enquanto o tempo de vida dele permitir)
- Mesmo fechando o navegador, o cookie permanece ativo.
- No segundo exemplo, vamos ter um formulário que envia o tempo de vida que atribuiremos ao cookie.

---

## Manipulação de Cookies

```html
<h4>Definiindo tempo de vida do cookie</h4>
<form action="{{url_for('cookie2')}}" method="post">
    <input type="text" placeholder="tempo em segundos" name="time">
    <input type="submit" value="Enviar">
</form>
```

```python
@app.route("/cookie2", methods=['POST'])
def cookie2():
    text = "<h1>Um cookie foi definido<h1/>"
    time = int(request.form['time'])
    response = make_response(text)
    response.set_cookie('primeiro_cookie', 'teste', max_age=time)
    return response
```

---

## Manipulação de Cookies

- No código HTML, temos um formulário simples que envia dados via HTTP POST: vamos enviar o tempo em segundos
- Obtemos o dado e convertemos para inteiro
`time = int(request.form['time'])`
- Criamos o response
`response = make_response(text)`
- Definimos o retorno
`response.set_cookie('primeiro_cookie', 'teste', max_age=time)`

---

## Manipulação de Cookies

<style scoped>
    table {
        font-size: 32px
    }
</style>

- Parâmetros adicionais para cookies

| Parâmetro | Caracaterísica                                               |
|-----------|--------------------------------------------------------------|
| httponly  | Não permite o acesso ao cookie via Javascript                |
| secure    | Indica que o cookie está diponível apenas em conexão HTTPS   |
| path      | Especifica um caminho para o cookie, por exemplo "/teste"    |
| domain    | Especifica um domínio específico, por exemplo www.domain.com |

---

## Manipulação de Cookies

- Eliminando acesso do Javascritp aos cookis com `http_only` 



---


## Manipulação de Cookies



- segurança (paâmetros)
- ONde encontrar no navegador

- Acesse cookies via `request.cookies`
- Defina cookies com `response.set_cookie`

---

<style scoped>
    section {
        display: flex;
        flex-direction: column;
        justify-content: center;
        text-align: center;
    }
</style> 

# Sessões 

---

## Sessões

- Use `session` para gerenciamento de sessões
- Necessita de uma chave secreta

---

