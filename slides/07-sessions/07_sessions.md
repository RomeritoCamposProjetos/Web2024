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

- É possível resolver este problema utilizando Sessões?
    - Sim
    - Podemos ter uma solução ainda melhor.

- O exemplo a seguir ilustra uma possível solução
--- 

## Sessões



---

## Sessões

---

