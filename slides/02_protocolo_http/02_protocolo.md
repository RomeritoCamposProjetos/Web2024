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
<!-- 
centrarlizar slide
<style scoped>
    section {
        display: flex;
        flex-direction: column;
        justify-content: center;
        text-align: center;
    }
</style> 

<style scoped>   
    h2 {
        text-align: center;
        font-size: 15px;
        margin-top: 450px;
    }
</style>
-->


# Conteúdo

- Protocolo HTTP
  - Introdução
  - Métodos
  - Funcionamento geral

---
<style scoped>
    section {
        display: flex;
        flex-direction: column;
        justify-content: center;
        text-align: center;
    }
</style> 

# Introdução ao HTTP
---

# Introdução ao HTTP

- HTTP = **Hyper Text** Transfer Protocol
  - Protocolo de Transferência de Hipertexto
  - *Hipertexto não é exclusivo do meio digital*

- É a base da web e permite obter recursos como documentos HTML

- Hypertext: [Vídeo sobre Hipertexto](https://www.youtube.com/watch?v=7bF6SwRqcFg)
  
- Hypermedia: [Vídeo sobre Hipermídia](https://www.youtube.com/watch?v=yfJrNnNLDbY)

---

<style scoped>   
    h2 {
        text-align: center;
        font-size: 15px;
        margin-top: 450px;
    }
</style>

# Introdução ao HTTP

![bg vertical 40%](./hipertexto-21.png)

## Fonte: https://estertecnoeducacao.blogspot.com/2012/06/o-uso-da-tecnologia-na-educacao.html

---

# Introdução ao HTTP

- É um protocolo de camada de aplicação para transmissão de documentos hipermídia
- Baseado em um modelo ***client-server*** (cliente e servidor)
- Tem como base pedidos realizados por clientes:
  - ***Requests*** (requisições)
- É um protocolo sem estado
  - O servidor não mantém informações entre requisições
---

# Introdução ao HTTP
<style scoped>   
    h2 {
        text-align: center;
        font-size: 15px;
        margin-top: 450px;
    }
</style>

![bg vertical 58%](./fetching_a_page.png)

## Fonte: https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Overview

---

# Introdução ao HTTP

- HTTP é o protocolo que permite obter **recursos**
  - Documentos HTML
  - Imagens
  - PDF etc

- As requisições sempre são iniciadas pelo cliente
- Um cliente pode ser um navegador Web ou um comando como [curl](https://curl.se/).

---

# Introdução ao HTTP
<style scoped>   
    h1 {
        margin-top: -40px
    }
    h2 {
        text-align: center;
        font-size: 15px;
        margin-top: 500px;
    }
</style>
<!-- # Introdução ao HTTP -->

![bg vertical 100%](./Request.png)

## Fonte: própria.

---

# Recursos, URL, URI

<style scoped>
    section {
        display: flex;
        flex-direction: column;
        justify-content: center;
        text-align: center;
    }
</style> 

---
# Recursos, URL, URI


https://www.alura.com.br/artigos/desmistificando-o-protocolo-http-parte-1#recursos-urls--e-uris

---

<style scoped>
    section {
        display: flex;
        flex-direction: column;
        justify-content: center;
        text-align: center;
    }
</style> 

# Requesições

---

# Requesições

---
# Referências

https://developer.mozilla.org/pt-BR/docs/Web/HTTP

URI
https://techenter.com.br/o-que-sao-uri-url-e-urn/