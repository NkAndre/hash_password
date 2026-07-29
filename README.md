# Hash Password with Bcrypt 🔐


Este é um projeto simples em Python desenvolvido para demonstrar como realizar o hashing seguro de senhas utilizando a biblioteca `bcrypt`. O script captura a entrada do usuário, converte os dados para o formato correto (bytes), gera um *salt* aleatório e valida a senha em uma simulação de login.

---

## 🚀 Tecnologias Utilizadas

* **Python 3.8+**
* **Bcrypt**: Biblioteca para derivação de chaves e hashing seguro.

---

## 📋 Pré-requisitos e Instalação

Antes de executar o projeto, você precisa ter o Python instalado em sua máquina e instalar a dependência do projeto.

1. Instale o `bcrypt` via terminal/PowerShell:
   ```bash
   pip install bcrypt
   ```
---

## 🛠️ Como Executar o Projeto


1. Clone o repositório : git clone https://github.com/NkAndre/hash_password.git
   ```bash
    cd hash_password
   ```

2. Execute o script principal:
   ```bash
   python main.py
   ```

3. Siga as instruções na tela: digite uma senha para criptografar e, em seguida, digite-a novamente para testar a verificação de login.

---

## 📝 Como funciona o código?

O `bcrypt` exige que os dados textuais (*strings*) sejam convertidos em blocos de dados binários (*bytes*). O script resolve isso utilizando a codificação UTF-8:

* **Criptografia:** `senha.encode('utf-8')` transforma o texto em bytes antes de gerar o hash.
* **Exibição:** `.decode('utf-8')` transforma o hash gerado de volta em texto legível para exibição no terminal.
