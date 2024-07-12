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

---

<style scoped>
    section {
        display: flex;
        flex-direction: column;
        justify-content: center;
        text-align: center;
    }
</style>

# Ambiente Virtual para o Flask

---

## Passos para Criar um Ambiente Virtual

1. **Instalação do virtualenv**
   - Se ainda não tiver o `virtualenv` instalado, você pode instalá-lo usando o `pip`:
     ```bash
     pip install virtualenv
     ```

---

## Passos para Criar um Ambiente Virtual

2. **Criação do Ambiente Virtual**
   - Navegue até o diretório onde deseja criar o ambiente virtual e execute o seguinte comando para criar um ambiente virtual chamado `venv`:
     ```bash
     virtualenv venv
     ```

---

## Passos para Criar um Ambiente Virtual

3. **Ativação do Ambiente Virtual**
   - No Windows, ative o ambiente virtual usando:
     ```bash
     venv\Scripts\activate
     ```
     No macOS/Linux, use:
     ```bash
     source venv/bin/activate
     ```

---
## Passos para Criar um Ambiente Virtual

4. **Instalação do Flask**
   - Com o ambiente virtual ativado, instale o Flask usando o `pip`:
     ```bash
     pip install flask
     ```

---

## Utilizando o Ambiente Virtual

- Com o ambiente virtual ativado, você pode desenvolver e executar aplicativos Flask sem interferir nos pacotes globais do sistema.
- Sempre ative o ambiente virtual antes de trabalhar com seu projeto Flask para garantir que todas as dependências sejam isoladas e gerenciadas corretamente.

