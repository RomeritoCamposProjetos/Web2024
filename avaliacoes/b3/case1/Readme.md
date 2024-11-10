Considere o código-fonte em anexo que está com uma aplicação adotando o padrão MVC. Esta aplicação não possui login de usuários. Você deve adicionar um módulo independente a esta aplicação que permite incluir o login de usuários na aplicação. Este módulo deve estar armazenado em um pacote chamado `auth`. Dentro de auth crie um arquivo `bp.py` que deve conter um blueprint. Abaixo segue os detalhes dos requisitos e pontuação.

## Orientações Gerais

1. Baixar o arquivo do código da avaliação.
2. Instalar os pacotes presentes em `requirements.txt`.
3. Rodar a aplicação e incluir os requisitos listados abaixo.
4. A aplicação já possui rotas funcionais.
5. **Ao enviar o projeto, deve-se anexar todo o conteúdo. INCLUINDO a pasta env.**

## Requisitos

1. (5 pontos) Adicionar módulo auth
    1. Criar templates de login
    2. Criar arquivo blueprint `bp.py`
2. (5 pontos) Adicionar `login_manager` em [`bp.py`](http://bp.py)
3. (5 pontos) Definir o `user_loader` do `login_manager` conforme o código abaixo

```python
@login_manager.user_loader
def load_user(user_id):
    return User.find(id=user_id)
```

4. (5 pontos) Criar o blueprint `auth_bp`
    1. O diretório de `templates` deve ser dentro de `auth`
5. (30 pontos) Definir duas rotas no blueprint `auth_bp`
    1. Login
        1. Loga o usuário
        2. Redireciona para index de usuários
    2. Logout
        1. Apenas requisições POST
        2. Redireciona para index do projeto
6. (10 pontos) Proteger a rota index de `users` contra acesso de usuários não autorizados
7. (20 pontos) Proteger todas as rotas de `books`
8. (10 pontos) Importar o blueprint em `app.py`
    1. Definir `secret_key` necessário do `login_manager`
    2. Inicializar a o login_manager com app: `login_manager.init_app(app)`
9. (10 pontos) Registrar o blueprint em `app`