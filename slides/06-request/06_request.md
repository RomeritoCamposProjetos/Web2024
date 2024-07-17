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

## Manipulação de COokies




---

## Manipulação de Cookies

- como funcionam (exemplo alura)
    - estudo de caso: manter prefereências de cor de pagina para usuário
- tipos de cookies
    - cookies de sessão 
        - expiram ao fechar o navegador
    - permanent cookies
        - permanecem
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

