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
  
---

## Conteúdos

- Instalação e Configurações
- Modelos
- Engine
- Sessão
- Consultas básicas
  - select
  - update
  - delete

---

## Instalação e configuração

- instar
  
> pip install sqlalchemy


## Sessão

In the most general sense, the Session establishes all conversations with the database and represents a “holding zone” for all the objects which you’ve loaded or associated with it during its lifespan

The ORM objects maintained by a Session are instrumented such that whenever an attribute or a collection is modified in the Python program, a change event is generated which is recorded by the Session. 