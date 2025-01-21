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

- Objetivo: realizar consultas utilizando o ORM SQLAlchemy
  
---

## Conteúdos

- Consultas 

---

<style scoped>
    section {
        display: flex;
        flex-direction: column;
        justify-content: center;
        text-align: center;
    }
</style> 

# Realizando consultas

---
## Realizando consultas

- O SQLAlchemy oferece funções para realização de consultas ao banco utilizando `select`. 

- Além disso podemos realizar `insert`, `delete` e `update` utilizando orientação ao objetos e as informações de definição de modelos.


- O [exemplo 04](https://github.com/RomeritoCamposProjetos/Web2024/tree/main/slides/15_ORMS/case4) mostra o código utilizado para realizar algumas operações comuns em SQL através de `session`.

---

## select

- A operação de SELECT pode ser feita pela função `select`.

- Selecione todos os usuários do banco:
```python
from sqlalchemy import select
# demais importes, engine e session omitidos

declaracao_sql = select(User)
session.execute(declaracao_sql).scalars().all()
```

- A função `select` vai construir uma declaração SQL que pode ser executada. 

---

- A execução da consulta tem algumas chamadas encadeiadas de funções.

- Primeiro executamos a função `execute(declaracao_sql)`. Em seguida, executa-se a função `scalars()`.

- A função `scalars`