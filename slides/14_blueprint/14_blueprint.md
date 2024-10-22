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

- Objetivo: aplicar o recurso Blueprint do Flask para modularizar aplicações
  
---

## Conteúdos

- Definição
- Aplicação

---

<style scoped>
    section {
        display: flex;
        flex-direction: column;
        justify-content: center;
        text-align: center;
    }
</style> 

# Blueprints

---

# Blueprints

- O Conceito de Blueprints é utilizado para dar suporte a padrões e criação de componetes de uma aplicação
- Um objeto Blueprint funciona de forma semelhante a um objeto Flask, mas não representa em si uma aplicação.
- Podemos utilizar blueprints quando:
    - refatorar aplicações grandes em componentes
    - criar extensões flask
    - registrar blueprints sob diferentes prefixos de URL

---

# Blueprints

- O funcionamento básico de um Blueprint consiste em criar operações para este blueprint via funções `view`.
    - Estas funções são aquelas que definimos para uma rota.
- Uma vez que estas operações são definidas no Blueprint podemos vinculá-las as aplicações registrando o Blueprint no `app`.

- Neste material, vamos explorar dois estudos de caso nos quais Blueprints são aplicados.
- Sugestão de leitura: [1](https://flask.palletsprojects.com/en/3.0.x/blueprints/), [2](https://www.digitalocean.com/community/tutorials/how-to-structure-a-large-flask-application-with-flask-blueprints-and-flask-sqlalchemy) e [3](https://www.freecodecamp.org/news/how-to-use-blueprints-to-organize-flask-apps/)

---

<style scoped>
    section {
        display: flex;
        flex-direction: column;
        justify-content: center;
        text-align: center;
    }
</style> 

# Blueprint
## Estudo de Caso 1
---

# Blueprint

- Neste exemplo, vamos considerar o exemplo que já conhecemos para cadastro de usuários.

- Requisitos:
    - Cadastrar usuário
    - Listar usuários

- Adicionamento, vamos também atender aos seguintes requisitos:
    - Cadastrar livros
    - Listar livros

---
```bash
# Estrutura do Projeto
case1/
├── app/
│   ├── __init__.py
│   ├── templates/
│   │   ├── layout.html
│   │   └── auth.html
│   └── app.py
├── books/
├── users/
│   ├── __init__.py
│   └── templates/
│       └── users/
│           ├── index.html
│           └── register.html
├── database/
└── app.py
```

---

# Blueprints

- No slide anterior, há um esboço do projeto: código-fonte.

O projeto está dividido em:
- `app/`: diretório da aplicação, iniciamos o `app = Flask(__name__)`
- `users`: todos os recursos de usuário do exemplo (rotas, modelo e páginas)
- `books`: o mesmo que users.
- O arquivo `app.py` que é o último listado é utilizado para `flask run`

---

# Blueprints

- Para rodar este exemplo basta; `flask run --debug`
    - considere que você já iniciou o banco da aplicação
- É importante afirmar que esta divisão dos diretórios não é meramente com base no uso de pacotes.
- Neste estudo de caso, utilizamos um recurso importado do flask.
```python
from flask import Blueprint
``` 
- A classe `Blueprint` permite modularizar a aplicação.

---

# Blueprints

- Mas o que de fato é um Blueprint? O que podemos fazer com ele?
- Vamos examinar a pasta `users` e seus arquivos.
- A pasta `users` é um pacote python (veja o arquivo `__init__.py`).
- Além disso, nesta pasta teremos o seguinte:
    - `users.py`: módulo python chmado `users`;
    - `templates`: local dos templates de `users`;
    - `models.py`: modelos referente a usuários (apenas um no momento).

---

## Criação de Blueprint

- Esta estrutura representa basicamente todos os recurso de uma aplicação flask. É uma estrutura autocontida.
- Entretanto, ela não é uma aplicação em si.
- O arquivo `users` inicia com as seguintes linhas.
```python
from flask import render_template, Blueprint, url_for, request, flash, redirect
from users.models import User

# módulo de usuários
bp = Blueprint('users', __name__, url_prefix='/users', template_folder='pages')
```
---

- Observe que não importamos a classe Flask porque não vamos iniciar a aplicação (que sempre guardamos numa variável `app`) neste arquivo.
- Importamos alguns recurso do flask (em especial `Blueprint`).
- Em seguida, definimos um blueprint e guardamos em `bp`.
- Neste exemplo, a classe Blueprint recebeu 4 argumentos:
    - `users`: nome do blueprint
    - `__name__`: import_name que é nome usado para importação (nome do arquivo python)
    - `url_prefix`: prefixo a ser adiciona a url das rotas (veremos)
    - `template_folder`: local onde ficam os arquivos HTML
---

<style scoped>
ul + p {
    background-color: yellow;
    height: fit-content;
    text-align: center;
    padding: 5px 0;
    border-radius:25px;
}
</style>

- A questão é: o que fazer com o objeto `bp`? A abaixo esta resposta:

```python
@bp.route('/')
def index():
    return render_template('users/index.html', users = User.all())
```
- Definimos uma rota vinculada a este Blueprint. Esta rota usa uma `view` chamada `index`.
- Dentro da rota temos o uso de um modelo chamado `User`

A definição da rota não indica que ela já está disponível para uso. É necessário registrá-la na aplicação.

---

## Importanto o Blueprint

- Após a criação do Blueprint devemos importá-lo no destino.
- O atributo que indica o nome de importação é o `import_name`, que no exemplo é `__name__`. Ou seja, o nome do próprio arquivo (`users.py`)
- Neste exemplo, vamos impotar no arquivo da aplicação conforme abaixo:

```python
# trecho de app/__init__.py
from users import users
```

---

## Registrar Blueprint

- O próximo passo é registrar este Blueprint.
- Isso deve ser feito na aplicação. A aplicação foi criada no pacote `app` dentro do arquivo `__init__.py`. Abaixo o trecho que registra o Blueprint.

```python
# trecho de app/__init__.py
from flask import Flask, render_template
from users import users
from books import books

app = Flask (__name__, template_folder='templates')
app.register_blueprint(users.bp)
```

---
- Quando registramos o Blueprint na aplicação, estamos fazendo com que as funcionalidades definidas possam ser usadas na aplicação. 

- Neste caso, a funcionalidade do exemplo é uma rota.

- Um detalhe importante é o uso do argumento `url_prefix='/users'` na contrução do Blueprint.

- Isso significa que todas as rotas tem o prefixo `/users`:

```bash
http://localhost:5000/users/
http://localhost:5000/users/register
```
---

<style scoped>
ul + p {
    background-color: yellow;
    height: fit-content;
    text-align: center;
    padding: 5px 0;
    border-radius:25px;
}
</style>

## Recursos do Blueprint

- Uma atenção especial sobre os recursos como páginas e arquivos estáticos (css, icones e etc) deve ser dada.

- De acordo com a documentação do Flask sobre a pasta templates, temos:

Flask vai procurar pelos templates em uma pasta templates. Se a aplicação é um módulo, a pasta estará perto do módulo, se for um pacote está dentro do pacote.

---

- Neste estudo de caso, a aplicação está dentro de um pacote. 
- Logo, a pasta templates está dentro deste pacote:

```bash
case1/
├── app/
    ├── __init__.py
    ├── templates/
    │   ├── layout.html
    │   └── auth.html
    └── app.py
```

- O que isso tem a ver com Blueprints? No exemplo de uso de Blueprints temos arquivos HTML. Logo, precisamos decidir onde colocá-los.

---

- Você já observou que colocamos os arquivos HTML do Blueprint `usesr` dentro do pacote `users`. 

- Veja a pasta `users\templates\users`. Ela contém dois arquivos HTML que usamos para usuários.

- Veja o Blueprint
```python
bp = Blueprint('users', __name__, url_prefix='/users', template_folder='templates')
```

- O argumento `template_folder` indica que vamos salvar os templates do blueprint dentro de uma pasta templates que se localiza no pacote do Blueprint.

---

- Entretanto, o Flask vai procurar os templates para a função `render_template` nos diretórios registrados para conter templates, que são:
    - templates dentro do pacote da aplicação
    - demais pastas de templates dos Blueprints
- Isso significa que devemos evitar nomes que gerem conflitos.
- Por esta razão a pasta de templates do Blueprint é na verdade:
```bash
users\templates\users
```

- Toda explicação dada aqui serve para o Blueprint `books`.

---

## Blueprint e Modelos

- Neste exemplo, o pacote `users` contém um moódulo chamado `models`.

- Este módulo contém uma class `User` que foi utilizada pelo Blueprint para realizar operações no banco de dados.

- Nas duas rotas do exemplo, temos a utilização do Modelo.

- Basta um simples import para o modelo Ser utilizado:

```python
# trecho de users.py
from users.models import User
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

# Estudo de Caso 2
## Blueprint e MVC

---

- 