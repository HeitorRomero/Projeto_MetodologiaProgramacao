# 🏥 Sistema de Diagnósticos Médicos

## 💻 Sobre o Projeto
Este é um sistema de controle e gerenciamento hospitalar desenvolvido inteiramente em **Python** via linha de comando (CLI). Foi o projeto final (Etapa 4) desenvolvido para a disciplina de Metodologia e Programação. 

O objetivo do sistema é gerenciar o fluxo de atendimento médico, conectando Pacientes, Equipes Médicas, Exames e Diagnósticos através de um menu interativo, com persistência de dados em arquivos locais.

## ⚙️ Principais Funcionalidades
* **Gerenciamento de Entidades:** Cadastro e leitura de Pacientes e Equipes Médicas.
* **Relacionamentos Complexos:** Controle de Exames (relacionamento 1:N com Pacientes) e Diagnósticos (Entidade Associativa entre Paciente e Equipe Médica).
* **Ordenação de Dados:** Algoritmos de ordenação baseados em funções lambda, permitindo classificar exames por data, gravidade ou múltiplos atributos simultaneamente.
* **Persistência de Dados:** Leitura de carga inicial via `JSON` e exportação do histórico de operações e logs para arquivo de texto (`.txt`).
* **Tratamento de Exceções:** Interface robusta contra erros de digitação e falhas de I/O.

## 🛠️ Tecnologias e Conceitos Utilizados
* **Linguagem:** Python 3
* **Paradigma:** Programação Orientada a Objetos (POO)
* **Estruturas de Dados:** Listas, Dicionários e manipulação de Objetos.
* **Armazenamento:** JSON e TXT.

## 🚀 Como Executar
1. Clone este repositório.
2. Navegue até a pasta do controlador: `cd src/controle`
3. Execute o programa principal: `python3 projeto.py`
4. Interaja com o menu numérico no terminal. O histórico de uso será salvo na pasta `dados`.
