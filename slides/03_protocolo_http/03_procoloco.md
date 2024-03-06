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
    pre {
        float: left;
        width: 45%;
        margin-right: 5px;
        margin-top: 0px
    }
---

![w:120 h:120](../../assets/ifrn-vertical.png)
# Programação de Sistemas para Internet
Prof. Romerito Campos

---

# Plano de Aula

- Objetivo: 
  - Compreender o funcionamento de formulários, métodos GET e POST e strings de consulta

- Conteúdo:
  - Métdos POST e GET
  - Formulários HTML
  - Strings de Consulta

---

# Metodos GET e POST

- Métodos **GET** tem por objetivo permitir que uma representação de recurso especificado seja recuperado

- Método **POST** tem por objetivo enviar dados para o servidor.
  - Este método tem detalhes adicionais em relação ao método GET
  - Uma forma comum de enviar requisições POST é via **Forms HTML**
  - Também é possível realizar via javascript

---
<style scoped> 
    section {
        display: flex;        
        justify-content: center;
        flex-direction: column;
        align-items: center;        
    }
</style>

# Método POST

---

# Método POST

- Request são geralmente enviadas via formulários HTML
  - `<form> ... </form>`
- Quando precisamos realizar algum tipo de alteração no servidor, utilizamos POST.
  - Salvar algum dado, por exemplo
  - Login/logout de usuários também são exemplos (*mesmo ser alterar dados no servidor*)

---

# Metodo POST

<style scoped>
    pre > * {
      font-size: 40px
    }
    pre {
        float: left;        
        width: 100%;
        margin-right: 5px;
        margin-top: 0px
    }
</style>

- Podemos indicar o tipo de conteúdo a ser enviado
  - **application/x-www-form-urlencoded**
  - **multipart/form-data**

- Estas opções podem ser passadas via `enctype` no html

```html
<form ectype="multipart-form-data">   
  <input type="file"> 
</form>
```
---

# Método POST


<style scoped>
    pre > * {
      font-size: 40px
    }
    pre {
        float: left;        
        width: 100%;
        margin-right: 5px;
        margin-top: 0px
    }
</style>

- **application/x-www-form-urlencoded (PADRÃO)**: codifica a informação entre pares de valores separados por *&*

- Dado um formulário com três campos: nome, cidade e idade. A informação é codificada como abaixo:

```plain
Nome=rafael&cidade=campinas&idade=3
```
---

# Método POST

- **multipart/form-data**: 
  - mais flexível [1](https://pt.stackoverflow.com/a/103169), [2](https://reqbin.com/req/yjok4snr/post-html-form-example).
  - Pode ser utilizado para envio de dados binários como imagens além de texto.
  - Acrescenta overhead no processamento no servidor (pouco indicado para dados textuais)

---

# String de Consulta

<style scoped> 
    section {
        display: flex;        
        justify-content: center;
        flex-direction: column;
        align-items: center;        
    }
</style>

---
# String de Consulta

<style scoped>
    pre > * {
      font-size: 40px
    }
    pre {
        float: left;        
        width: 100%;
        margin-right: 5px;
        margin-top: 0px
    }
</style>

- Strings de consulta estão fortemente relacionadas ao médoto GET

- É possível ver sua composição na URL através da barra de navegação

- Podemos observar também na construção de links

```htm
http://localhost:5000/profile?name=joao&sname=jj
```

---

# String de consulta

<style scoped>
    pre > * {
      font-size: 40px
    }
    pre {
        float: left;        
        width: 100%;
        margin-right: 5px;
        margin-top: 0px
    }
</style>

- Úteis para criação de filtros
- Envio de dados ao servidor (dados não-sensíveis)

```htm
http://localhost:5000/profile?name=joao&sname=jj
```

- String de consulta
  - Utiliza-se **?** seguido de pares **key=value** separados por **&**
```htm
/profile?name=joao&sname=jj
```

---

# Prática

---

# Atividade

---

# Referências

<style scoped>
  p {
    font-size: 24px
  }
</style>

CODINGSCENES. What is the difference between application/x-www-form-urlencoded and multipart/form-data OR text/plain? Disponível em: <https://medium.com/@codingscenes/application-x-www-form-urlencoded-and-multipart-form-data-are-two-different-formats-for-3678a10073e9>. Acesso em: 6 mar. 2024.


MIME types. Disponível em: <https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Basics_of_HTTP/MIME_types>. Acesso em: 5 mar. 2024.


POST. Disponível em: <https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Methods/POST>. Acesso em: 5 mar. 2024.

