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
    - Compreender o uso de Sessions em Flask

---

## Conteúdos

- Cookies (veja aula sobre cookies) - [Link](../06-request/06_request.pdf)
- Sessões
- Mensanges Flash

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

- Premissas:
    - HTTP é um protocolo sem estado
    - Cada request é independente uma da outra
    - A comunicação cliente servidor é baseada em Request-Response

- **Como podemos permitir que uma requisição possa ter relação com anterior nestas condições?**
    - A resposta para a pergunta apresentada no slide anterior é o uso de *Sessões*
---

## Sessões


- As sessões permitem manter informações sobre o uso do usuário durante múltiplas requisições
- Exemplos:
    - e-commerce, redes sociais, sistemas escolares

- Todos esses exemplos e muitos outros permitem ao interessados a criação de contas de usuário 
- Estas contas permitem que os ususuários ingressem no serviço e iniciem **sessões**

---

## Sessões

- Características:
    - são construídas sobre os cookies (utiliza-os);
    - armazenam informações do usuário entre requisições;
    - Os cookies são assiandos criptograficamente (mais segurança);

- No framework flask, vamos usar um objeto chamado `session` e também configurar uma chave utilizada para realizar a criptografia dos cookies. 

```python
app.config['SECRET'] = 'super chave'
 ```
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
## Estudo de Caso - Prova

---
<style scoped>
    section * {
        text-align: justify
    }
</style>

## Sessões

- Considere o desafio abaixo:
Desenvolver uma aplicação que permite o envio de mensagens por usuário logado. Quando um usuário estiver logado, ele poderá acessar uma página com um formulário e enviar uma mensagem de texto. Fluxo de execução: acessar página inicial; clicar no link de login e ser enviado para uma página com formulário e adicionar o nome de usuário; a partir desde momento, o usuário pode acessar uma página de cadastro de mensagens em seu nome e enviar mensagens; haverá uma página de mensagem.

---

## Sessões

- Considerações iniciais
    - precisamos de uma maneira de armazenar informações de modo que os dados não sejam perdidos durante as requisições
    - já temos um recurso para isto: **cookies**
    - como alternar entre usuários difererentes e não perder as informações?
    - adicionaremos uma lista no contexto da aplicação (não se apaga durante sua execução)

- O código deste exemplo está no repositório: [Aqui](../07-sessions/login_cookies/)

---

## Sessões

- Trecho da View **mural** para requisições GET

```python
@app.route('/mural', methods=['POST', 'GET'])
def mural():
    if request.method == 'GET':
        name = request.args.get('name')
        lista = []
        if name and name in mensagens.keys():
            lista = mensagens[name]
        return render_template('mural.html', lista=lista)
```

---

## Sessões

- A view **mural** atende requisições GET garantindo que vamos mostrar as mensagens filtradas pelo nome do usuário
- Para isto utiliza-se **string de consulta**

```python
# o trecho recupera o dado passado na URL
# localhost:5000/mural?name=teste
name = request.args.get('name')
```

- Neste caso, a variável `name` tem conteúdo 'teste'.
- O if a seguir no código verifica se a lista `mensagens` possui a chave 'teste' e pega as mensagens vinculadas 

---

## Sessões

- Enviar uma mensagem requer um processamento mais complexo:
```python
    # trecho do código da view 'mural'
    else:
        name = request.form['name']
        message = request.form['message']
        if name in mensagens:
            mensagens[name].append(message) 
        else:
            mensagens[name] = [message]
        if 'name' in request.cookies and request.cookies['name'] == name:
            return render_template('mural.html', lista = mensagens[name])
        else:
            response = make_response(render_template('mural.html', lista = mensagens[name]))
            response.set_cookie(key='name', value=name)
            return response
```

---

## Sessões

- O primeiro passo é recuperar os dados do formulário
```python
name = request.form['name']
message = request.form['message']
```
- Em seguida, adicionar a mensagem a lista de mensagems do usuário
```python
if name in mensagens:
    mensagens[name].append(message) 
else:
    mensagens[name] = [message]
```

---

## Sessões

- POr fim, verificarmos se existe cookie e criamos um se for necessário

```python
if 'name' in request.cookies and request.cookies['name'] == name:
    return render_template('mural.html', lista = mensagens[name])
else:
    response = make_response(render_template('mural.html', lista = mensagens[name]))
    response.set_cookie(key='name', value=name)
    return response
```

---

## Sessões

- O bloco de código referente ao envio de mensagens pode tem o seguinte comportamento:
    - Enquanto um usuário estiver mandando mensagem, o cookie terá seu nome
    - quando um novo usuário mandar mensagem o cookie passa a representar o novo usuário
    - a variável `mensagens` garante a manutenção das mensagens mesmo com a mudança de usuários

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
## Estudo de Caso - Prova com Sessões

---

## Sessões

- É possível resolver este problema utilizando Sessões?
    - Sim
    - Podemos ter uma solução ainda melhor.

- O exemplo a seguir ilustra uma possível solução

- [Aqui](../07-sessions/problema_session/) você encontra o código completo
--- 

## Sessões

- O framework Flask possui um objeto chamado `session`
- Este objeto armazena um cookie criptografado no lado do cliente(navegador)
- Ele também permite armazenar dados na sessão do usuário
- No exemplo desta aula, vamos recriar o código das mensagens usando sessão de usuários

- A seguir veremos a parte crucial da implementação


---

## Sessões

- Objeto `session` é uma lista que permite a adição de itens e consulta sobre o que está armazenado.

- Para adicionarmos algum dado a sessão basta:
```python
session['user'] = 'romerito'
session['message'] = ['romerito', '1231']
```

- Verificar se existe uma chave na sessão: `'user' in session`
- Acessar elemento em uma sessão: `session['user']` 

---
## Sessões

- Para utilizar sesões o primeiro passo é importar o objeto `session`
```python
from flask import Flask, request, session, url_for, render_template, redirect
```

- Adicionar uma chave secreta:
```python
app = Flask(__name__)
app.config['SECRET_KEY'] = '123123123'
```

- A chave secreta deve ser mais forte e não pode ser compartilhada
---
## Sessões

- Tratamento para requisição GET

```python
@app.route('/mural', methods=['GET', 'POST'])
def mural():
    if request.method == 'GET':
        if 'name' in request.args:
            name = request.args.get('name')
        elif 'user' in session:
            name = session['user'] 
    
        lista = []
        if name in session.keys():
            lista = session[name]    
        return render_template('mural.html', lista=lista)
```

---

## Sessões

- Quando a página do mural de mensagem é acessada via GET, tentamos recuperar o nome do usuário via string de consulta:

```python
if 'name' in request.args:
    name = request.args.get('name')
elif 'user' in session:
    name = session['user'] 
```
- A cláusula `elif` é utilizada para verificar se existe um usuário (`user`) na sessão. Caso existe, o nome é obtido.
- Esse nome (`name`) é usado no próximo passo

---

## Sesssões

- Após obter algum `name` de usuário, tentamos recuperar suas mensagens:

```python
lista = []
if name in session.keys():
    lista = session[name]    
return render_template('mural.html', lista=lista)
```

- A cláusula `if` é usada para veriricar se existe alguma `chave` na sessão com o nome do usuário: `name in session.keys()`.
- se houver, uma `lista` é criada.

---

## Sessões

- Tratamento de requisições POST
```python
else:
    name = request.form['name']
    message = request.form['message']
    session['user'] = name
    if name in session.keys():
        session[name].append(message)
    else:
        session[name] = [message]
    return render_template('mural.html', lista=session[name])
```

---

## Sessões

- O primeiro passo no tratamento de requisições POST é obter as informações enviadas nos formulário:
```python
name = request.form['name']
message = request.form['message']
session['user'] = name
```
- Na linha `session['user'] = name` definimos o usuário da sessão

- O proximo passo é tratar a mensagem enviada

---

## Sessões 

- Adicionar mensagem a sessão

```python
if name in session.keys():
    session[name].append(message)
else:
    session[name] = [message]
return render_template('mural.html', lista=session[name])
```

- o `if` é utilizado para verificar se já existe uma lista de mensagem para o usuário `name`. Se sim, adicionar a mensagem a lista.
- Caso contrário, vamos criar uma lista vinculada ao user já na sessão.

---

