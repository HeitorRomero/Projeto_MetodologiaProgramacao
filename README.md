# 🏥 Diagnóstico de Exames de um Paciente por uma Equipe Médica

## 💻 Sobre o Projeto
Sistema em **Python** (Programação Orientada a Objetos) para modelar o fluxo de diagnóstico médico, conectando Pacientes, Equipes Médicas, Exames e Diagnósticos. Desenvolvido para a disciplina de **Metodologia e Programação** (UFGD) — Etapa 3.

O programa cadastra pacientes, equipes médicas e diagnósticos em memória, e demonstra a listagem e ordenação dos exames de cada paciente.

## 🗂️ Modelo de Entidades

- **Paciente**: `nome`, `idade`, `gênero`, `exames` (1:N com Exame)
- **EquipeMédica**: `crm`, `especialidade` (cardiologia, neurologia, ortopedia, pediatria, podologia), `número_médicos`
- **Exame**: `código`, `urgência` (baixa, média, alta), `convênio`, `nível_gravidade`, `data`
- **Diagnóstico**: entidade associativa entre `Paciente` e `EquipeMédica`, com `data`

## ⚙️ Funcionalidades

- Cadastro de pacientes, equipes médicas e diagnósticos (dados de exemplo definidos em `projeto.py`)
- Impressão formatada de listas de objetos (`imprimir_objetos`)
- Ordenação de exames por um atributo (`ordenar_objetos_por_um_atributo`), ex.: por gravidade ou por data
- Ordenação de exames por dois atributos combinados (`ordenar_objetos_por_dois_atributos`), ex.: gravidade e data juntas
- Validação simples de campos com enumeração restrita (ex.: `especialidade` e `urgência` caem para "indefinida" se o valor não for válido)
- Classe `Data` própria, com comparação (`==`, `<`, `>`, etc.) e cálculo de idade a partir de uma data de referência

## 📁 Estrutura do projeto

```
src/
├── controle/
│   └── projeto.py          # ponto de entrada — cadastra dados e roda as demonstrações
├── entidades/
│   ├── paciente.py
│   ├── equipe_médica.py
│   ├── exame.py
│   └── diagnóstico.py
└── util/
    ├── data.py              # classe Data (datas e comparações)
    └── gerais.py            # impressão e ordenação genérica de objetos
```

## 🛠️ Tecnologias e Conceitos Utilizados

- **Linguagem:** Python 3
- **Paradigma:** Programação Orientada a Objetos (POO)
- **Estruturas de Dados:** Dicionários (`pacientes`, `equipes_médicas` indexados por chave) e Listas (`diagnósticos`)
- **Ordenação:** funções `lambda` como chave de ordenação, inclusive por múltiplos atributos

## 🚀 Como Executar

```bash
cd src/controle
python3 projeto.py
```

O programa imprime no terminal: as equipes médicas, os pacientes, os diagnósticos e, para cada paciente, seus exames em três visões (ordem original, por gravidade decrescente, por data crescente e por gravidade+data combinadas).

## 📌 Status

Etapa 3 do projeto — dados cadastrados diretamente no código (sem persistência em arquivo ainda) e sem menu interativo. Essas partes fazem parte das etapas seguintes da disciplina.

## Autor

Heitor Pardinho Romero — Engenharia de Computação, UFGD
