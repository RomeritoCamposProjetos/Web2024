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

- Objetivo: Compreender o padrão de design de arquitetura Model-View-Controller
    - 
---

## Conteúdos

- Padrão MVC
- Vantagens
- Componenents
    - Model
    - View
    - Controller
- Funcionamento

---


<style scoped>
    section {
        display: flex;
        flex-direction: column;
        justify-content: center;
        text-align: center;
    }
</style> 

# Padrão MVC

---

# Padrão MVC

- O MVC é uma sigla para o **padrão de projeto** Model-View-Controller. 

- Este padrão é amplamente utilizado no mundo do desenvolvimento de software

- O objetivo é permitir a escrita da apliacação com base em componentes distintos realizando a separação de preocupaçãos (*separation of concerns*)

- Os componentes básicos são: **Model**, **View** e **Controller**.

---

# Padrão MVC

- As vantagens apontadas são:
  - Separação de preocupações
  - Reusabilidade
  - Escalabilidade
  - Testabilidade
  - Manutenabilidade

- A ideia por trás do uso de padrões de projeto reside na experiências de muitos estudos de caso e a reconhecida eficácia na reutilização da solução (padrão).

---

# Padrão MVC

- Os componentes Model-View-Controller tem responsabilidades distintas como resumido abaixo:
  - **Model**: responsável pela lógica de negócio e trato com os dados da aplicação;
  - **View**: responsável pela apresentação dos dados da aplicação aos clientes;
  - **Controller**: orquestra a interação entre as partes Model e View.

- Estes componentes pode ser vistos como *camadas* distintas na estruturação do código.

---

# Padrão MVC

- Em um contexto de divisão clara entre frontend e backend. Podemos compreender os componentes do MVC da seguinte forma:
    - **Model**: lógica da aplicação que reside no backend
    - **View**: apresentação de dados que reside no frontend
    - **Controller**: orquestração entre frontend e backend

---

<style scoped>
    section {
        display: flex;
        flex-direction: column;
        justify-content: center;
        text-align: center;
    }
</style> 

# Padrão MVC e Frameworks

---

# Padrão MVC e Frameworks

- Muitos frameworks para desenvolvimento de aplicações Web tem na sua definição arqutitetura o padrão MVC.

- O exemplo mais notório é o [Laravel](https://laravel.com/).

- Você deve estar se pergundando e o Flask e o Django?

---

# Padrão MVC e Frameworks

- O Flask não é estrutura com base uma arquitetura definida. 

- De acordo com a documentação, [neste link](https://flask.palletsprojects.com/en/3.0.x/design/#what-does-micro-mean), o flask não assume algumas decesiões de projetos.

- Portanto, há liberdade total para decisões sobre como a aplicação será estruturada. Que camadas deve possuir entre outros fatores.

- Isso não impede que um projeto em Flask assuma uma arquitetura MVC e incorpore soluções já referenciadas pela comunidade.

---

# Padrão MVC e Frameworks

- E quanto ao Django? Aí já temos uma história diferente do Flask.

- O Django implementa uma derivação do MVC que é comumente chamada de MVT (Model-View-Template).

- A mudança é sutil, mas importante. Os novos componentes são:
  - Model: continua com a mesma semântica do MVC;
  - View: tem um papel realcionado ao de controlador, contém a parte da lógica de negócio.
  - Template: camada de apresentação de dados aos clientes (como a View no MVC).

---

# Padrão MVC e Frameworks

- É importante observar que os frameworks não definem os padrões. É exatamente ao contrário.

- O padrão MVC é uma absrtração que pode ser utilizada em um framework como Flask de modo a se reutilizar boas práticas e soluções para problemas recorrentes.

- Desta maneira, se justifica, por exemplo, a mudança incorporada no Djando onde alguns elementos do MVC clássico estão definidos.

---
<style scoped>
    section {
        display: flex;
        flex-direction: column;
        justify-content: center;
        text-align: center;
    }
</style> 

# Implementação de MVC com Flask
## Estudo de Caso 1

---

# Implementação de MVC com Flask