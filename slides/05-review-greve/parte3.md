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

- Rotas dinâmicas
- Passagem de dados para templates
- Variáveis em templates

---

<style scoped>
    section {
        display: flex;
        flex-direction: column;
        justify-content: center;
        text-align: center;
    }
</style>


# Rotas dinâmicas e Templates

---

## Explicação do Código

- Considere o código abaixo

```python
# rota dinâmica com string de consulta
@app.route('/rota-dinamica/<nome>')
def rota_dinamica(nome):
    return render_template('rota_dinamica.html', dado=nome)
```

---

## Funcionamento do Código

1. **Rota Dinâmica**:
   - `@app.route('/rota-dinamica/<nome>')`: Define uma rota dinâmica no Flask. O `<nome>` dentro da URL indica um parâmetro dinâmico que será passado para a função view.
   - Quando um usuário acessa uma URL como `/rota-dinamica/Joao`, o valor `Joao` será capturado e passado como argumento para a função `rota_dinamica(nome)`.

---

## Funcionamento do Código

2. **Função View**:
   - `def rota_dinamica(nome):`: Define a função view `rota_dinamica` que recebe o parâmetro `nome` da URL.
   - `return render_template('rota_dinamica.html', dado=nome)`: Renderiza um template HTML chamado `rota_dinamica.html` e passa o valor do parâmetro `nome` para o template como a variável `dado`.

---

## Papel do `render_template`

- **Importação e Uso**:
  - A função `render_template` é usada para renderizar templates HTML. No contexto desta aplicação, ela é importada do módulo `flask` (como vimos anteriormente) e usada para renderizar o template `rota_dinamica.html`.
  - O valor do parâmetro `nome` é passado para o template como `dado`, permitindo que o template utilize esse valor dinamicamente.

---

## Exemplo de Template (`rota_dinamica.html`)

- Veja como usamos no HTML (parte do código abaixo)

```html
<body>
    <h1>Olá, {{ dado }}!</h1>
</body>
```

- **Uso da Variável no Template**:
  - No template HTML, `{{ dado }}` é uma expressão Jinja2 que será substituída pelo valor passado pela função view. Assim, se a URL acessada for `/rota-dinamica/Joao`, o conteúdo renderizado será "Olá, Joao!".

---