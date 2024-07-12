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

# Conteúdo

- Aplicação mínima
- Definição de rotas
- Execução da aplicação

---

<style scoped>
    section {
        display: flex;
        flex-direction: column;
        justify-content: center;
        text-align: center;
    }
</style>

# Aplicação Mínima

---

## Criando uma aplicação Flask

```python
from flask import Flask

# criando uma aplicação
app = Flask(__name__)
```

- Importamos a classe `Flask` do módulo `flask`.
- Criamos uma instância da classe `Flask` e atribuímos à variável `app`. Esta instância será a nossa aplicação Flask.

---

## Definindo uma rota

```python
@app.route('/')
def index():
    return "Hello World"
```

- Usamos o decorador `@app.route('/')` para definir uma rota na raiz (`'/'`) do site.
- A função `index` é associada a esta rota e retorna a string "Hello World" quando acessada.

---

## Maneira de executar

Para executar a aplicação Flask, você pode descomentar e usar o seguinte código:

```python
if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)
```

- O bloco `if __name__ == '__main__':` garante que o servidor só será executado se o script for executado diretamente.
- `app.run(host='127.0.0.1', debug=True)` inicia o servidor web local no endereço `127.0.0.1` com o modo de depuração ativado.

---

## Maneira de executar

- Com o bloco `if __name__ == '__main__':`, execute:

```bash
flask run --debug
```

- Observe que neste caso o nome do arquivo da aplicação deve ser `app.py`

- Caso tenha outro nome. Por exemplo, `main.py`. Rode o comando abaixo:

```bash
flask --app main.py run --debug
```