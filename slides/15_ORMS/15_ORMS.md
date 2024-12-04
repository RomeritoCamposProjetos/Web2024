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

<style scoped>
    section {
        display: flex;
        flex-direction: column;
        justify-content: center;
        text-align: center;
    }
</style> 

# Instalação


---
## Instalação

- O SQLAlchemy é uma caixa de ferramentas para SQL e um Mapeador Objeto-Relacional em python.
- É independente de framework.
- Portanto, pode ser usado isoladamente em scripts como também em frameworks como Flask.
    - O flask possui uma extensão para SQLAlchemy
- Instalação:
```bash
pip install sqlalchemy
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

# Configuração

---
## Configuração

- A configuração SQLAlchemy depende da criação de uma conexão com o banco de dados (por exemplo sqlite, MySQL e etc).
- Para tanto, o SQLAlchemy define uma função em seu core chamada `create_engine`
```python
from sqlalchemy import create_engine
```
- Esta função recebe uma string que pode ser montada com base no banco de dados.
---

## Configuração

- Nos exemplos, deste material utilizei o SQLITE.
- Para criar uma conexão com o SQLITE e salvar os dados em arquivo basta:

```python
from sqlalchemy import create_engine

engine = create_engine("sqlite:///database.db")
```

A partir do momento que o objeto engine tem a conexão com o banco, poderemos criar as tabelas.

---

## Configuração

- O objeto `engine` é o ponto inicial para uma aplicação com SQLAlchemy e também o meio pelo qual a robusta API do ORM pode acessar o banco.
- A engine é configurada com base em dialetos. O SQLITE é um dialeto. O MYSQL é outro. [Neste link](https://docs.sqlalchemy.org/en/20/core/engines.html), há todos os dialetos.
- Na prática, usamos a função create_engine como uma fábrica de conexões.

---

## Configuração

- Exemplo com MYSQL
```python
# conexão com MYSQL
engine = create_engine("mysql://root:romerito@localhost/banco")
```
- Observe o formato da String que pode ser decomposta em:
    - Sistema de Gerenciamento do Banco: `mysql`
    - Usuário: `root` e senha: `romerito` 
    - Endereço do banco: `localhost`
    - Nome do banco: `banco` 

---

<style scoped>
    section {
        display: flex;
        flex-direction: column;
        justify-content: center;
        text-align: center;
    }
</style> 


## Executando SQL

---

## Executanto SQL

- Através da `engine`, podemos obter um objeto que é capaz de executar instruções em SQL no banco.
```python
# continuação do código anterior
connection = engine.connect()
```
- Com o objeto `connection`, podemos **aplicar instruções** SQL no banco. 

- Obviamente, precisamos criar as tabelas e isso será feito com este objeto. Esta será a primeira instrução a ser aplicada.

---

## Executando SQL

- O [exemplo 01](https://github.com/RomeritoCamposProjetos/Web2024/tree/main/slides/15_ORMS/case1) mostra como usar a engine para conecar com o banco e aplicar SQL. O código abaixo mostra como criar uma tabela no Banco:

```python
from sqlalchemy import create_engine, text
engine = create_engine('sqlite:///database.db')
connection = engine.connect() # uma das formas
sql = text("CREATE TABLE users IF NOT EXISTS(id INTEGER PRIMARY KEY)")
connection.execute(sql)
```
- O trecho acima é um resumo do que foi falado até aqui.

---
- Para executar instruções, primeiro devemos criar uma instrução. Por exemplo: `create table users`.
    - Para isso vamos usar uma funação do SQLAlchemy chamada `text`    
    - O código abaixo prepara o SQL a ser executado.
```python
from sqlalchemy import text
# código da engine e connection
sql = text("""CREATE TABLE users IF NOT EXITS""")
```

- Com o objeto `connection`, podemos executar a função `execute(sql)` e ter a construção da tabela. 


---

## Executando SQL

- Da mesma forma que podemos usar `connection` para criar as tabelas, podemos também realizar outras operações como `INSERT`.
- No [exemplo 01](https://github.com/RomeritoCamposProjetos/Web2024/tree/main/slides/15_ORMS/case1), temos a operação de inserção de dados.
```python
# prepara a inserção
insert = text("""INSERT INTO users(nome) VALUES(:nome)""")
connection.execute(insert, {'nome':'jose'})
```
- O trecho acima está resumido. Perceba que `:nome` indica que precisamos indicar o nome que será inserido no banco. O dicionário na funação `execute` recebe o nome `josé`.  

---

## Executando SQL

- Neste primeiro exemplo, utilizamos a `engine` que conecta com o banco de dados. 
- Criamos um objeto `connection` que permite executar instruções SQL como criar tabelas e realizar inserções de dados
- Estas operações foram realizadas com SQL bruto (***raw SQL***)
- Veremos adiante que essa há recursos mais interessantes para interagir com banco.

---

<style scoped>
    section {
        display: flex;
        flex-direction: column;
        justify-content: center;
        text-align: center;
    }
</style> 

# Sessão

---

## Sessão

- O [exemplo 02](https://github.com/RomeritoCamposProjetos/Web2024/tree/main/slides/15_ORMS/case2) modifica o exemplo 01 e incorpora o uso de Sessões.

- De acordo com a documentação do SQLAlchemy, as sessões são usadas para estabelecer uma conversação com o banco de dados.

- Ela representa uma área onde objetos são carregados e mantidos durante a sessão do usuário durante o tempo de vida ativo da sessão.

- Por exemplo, se você salva um dado de um objeto utilizando uma sessão e modifica este dado, a sessão detecta esta alteração.

---

## Sesssão

- Parece complexo do ponto de vista conceitual e realmente é. Entretanto, na prática o uso de sessões facilita bastante a codificação.

- Podemos executar instruções SQL bruta a partir das sessões da mesma forma que fizemos com a conexão obtida da engine no exemplo 01.


---

## Sessão

- Retomando o [exemplo 02](https://github.com/RomeritoCamposProjetos/Web2024/tree/main/slides/15_ORMS/case2), vamos focar apenas no que é diferente em relação ao exemplo 01.

- A primeira coisa que fazemos é importar a classe `Session`

```python
from sqlalchmey.orm import Session
```

- O detalhe da importação é que a classe `Session` pertence ao módulo `ORM`. Lembre-se da definição do que é o SQLAlchemy.

---

- Vamos, em seguida, criar um objeto `session`

```python
session = Session(bind=engine)
```

- Observe que continuamos utilizando a `engine` que é o ponto de acesso ao banco de dados. Vinculamos a engine a Sessão que estamos criando.

- O objeto session vai utilizar o banco que foi definido para a engine.

- No exemplo 02, vamos criar o banco de dados utilizando SQL bruto

---

- O código abaixo cria o banco de dados com uma tabela de usuários

```python
# trecho de app.py do Exemplo 02
from sqlalchemy import text
sql = text("""CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    nome TEXT NOT NULL)""")

# neste momento o banco é criado com a tabela de usuários
session.execute(sql)
```

- Observe qu a função `execute` fara o trabalho de criação do banco utilizando a engine, mas isso é feito indiretamente e internamente.

---

- O próximo passo do exemplo é executar alguma instrução de registro de dados de usuários no banco

- Novamente, será utilizado SQL bruto conforme o código abaixo:

```python
# trecho de app.py
insert = text("""INSERT INTO users(nome) VALUES(:nome)""")

session.execute(insert, {'nome':'zefa'})
```

- Observe a semelhante entre a operação com sessões e a operação do Exemplo 01 com a engine.

- Ainda não chegamos ao potencial do usso de sessões.

---

<style scoped>
    section {
        display: flex;
        flex-direction: column;
        justify-content: center;
        text-align: center;
    }
</style> 

# Sessões e Modelos

---
## Sessões e Modelos

- No [exemplo 03](https://github.com/RomeritoCamposProjetos/Web2024/tree/sqlalchemy/slides/15_ORMS/case3), alcançamos o mesmo resultado do Exemplo 02. Entretanto, incluímos um novo recurso que é o uso de Modelos.

- O SQLAlchmey na sua definição indica que ele é um Mapeador OBjeto-Relacional para python.

- O uso de Sessões com Modelos é a concretização dessa definida, além - **é claro** - de inúmeros outros recursos.

- Portanto, não faz muito sentido usar SQL Bruto como nos exemplos anteriores, se podemos utilizar algo diretamente em Orientação a objetos para manipular o banco de dados.

---

- A novidade do Exemplo 03 é incluir um novo arquivo com a definição de um modelo de usuários 

```python
# trecho de app.py
from models import Base, User
```

- A classe `Base` é uma classe definda no arquivo models.py cujo objetivo é servir de classe modelo para as nossas classe. 
    - A classe Base é fudamental pois ela vair permitir o mapeamento declarativo das tabelas e suas colunas de modo que o SQLAlchemy conheças essas definições
    - A classe `User` terá como modelo a classe Base

---

- O código do arquivo `models.py` define a classe `Base` e a classe `User`

```python
# código models.py
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    nome:Mapped[str]
```
---

- A classe Base herda da classe DeclarativeBase, que o SQLAlchemy utiliza como definição de Modelo padrão.
- A classe User utiliza o mapeamento declarativo. É definido o nome da tabela e dois atributos, que são:
    - id (chave primária)
    - nome do usuário
- `id: Mapped[int]`: indica que o `id` será mapeado para inteiro no banco escolhido (INTEGER para SQLITE).
- `mapped_column(primary_key=True)` é um complemento para a coluna `id`. Neste caso, indica que id é a chave primária
- `nome: Mapped[str]` é mapeado para `TEXT` no sqlite 

---

- Esta é a primeira parte da configuração de uso de Modelos com Sessões.

- Uma vez que temos os modelos e o objeto `session` definido no arqiuvo `app.py` podemos criar o banco.

- A criação do banco utiliza o registro de metadados acessível através da classe `Base`.

```python
# trecho de app.py
Base.metadata.create_all(bind=engine)
```

- Observe que utilizamos a engine vinculada a criação das tabelas no banco.

---

- A última é etapa é utilizar os modelos para criar objetos e persistir os dados no banco.

- O trecho de código abaixo cria um objeto e o adiciona ao banco.

```python
#trecho de app.py
usuario = User(nome='jose')
# o objeto session já criado anteriormente
session.add (usuario)
session.commit()
```

- Observe exemplo 03 na íntegra e perceba que não se trabalha com SQL Bruto. Isso é abstraído pelo SQLAlchemy e sua implementação do ORM.

---

- Se você acompanhou até aqui, compare os exemplos 2 e 3. 

- O exemplo 02 faz a criação de tabela e inserção de usuários. Isso é feito utilizando o objeto `session` e executando SQL definido diretamente no código

- O exemplo 3 cria a tabela e insere dados sem trabalhar com SQL Bruto. 

- O objetivo do ORM é permite que se trabalho exclusivamente com orientação a objetos e mesmo assim seja possível e - ***fácil*** - de manipular o banco de dados.

- Osmodelos podem ser mais detalhados que este exemplo.

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




