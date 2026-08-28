# 🧠 lógica-prep — Prática de Lógica e Raciocínio para Testes Técnicos

Banco de exercícios de **lógica, raciocínio e algoritmos** para treinar provas técnicas estilo **LeetCode/Xobin** (ex.: programa de estágio **Vem Ser DBC**).

Cada exercício é convertido para o formato de **programação competitiva**: **função pura + casos de teste**, com suporte bilíngue:
- **Python** → Pytest (`solution.py` + `test_solution.py`)
- **TypeScript** → Vitest (`solution.ts` + `solution.test.ts`)

Você escolhe a linguagem: **implemente a função no stub e rode os testes localmente.**

## Estrutura

```
lógica-prep/
├── mundo_1_fundamentos/                # Curso em Vídeo (Guanabara), exercícios 001-035
├── mundo_2_estruturas_de_controle/     # Curso em Vídeo (Guanabara), exercícios 036-071
├── logica/                              # exercícios clássicos de lógica/raciocínio (FizzBuzz, Two Sum, palíndromo…)
├── vem_ser_dbc/                         # espelha a prova Xobin do Vem Ser DBC (questões vazadas: Sudoku 4x4, prazo por pesos, Fibonacci decrescente, frequência; + temas de alta prioridade)
└── README.md
```

Cada exercício tem 5 arquivos: `README.md` (spec pt-BR com Edge Cases/Abordagem/Complexidade), `solution_<exercício>.py` + `test_<exercício>.py` (Pytest), `solution.ts` + `solution.test.ts` (Vitest). Nomes **únicos por exercício** para o `pytest` rodar a suíte toda.

> Pode criar novas pastas temáticas (ex.: `logica/`, `algoritmos/`, `strings/`, `matematica/`) e adicionar qualquer exercício de lógica que quiser — é só seguir o mesmo padrão de pasta.

## Pré-requisitos

- **Python 3.10+**
- **Node.js 18+**

## Setup

```bash
# Python
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt

# TypeScript
npm install
```

## Rodar os testes (local)

```bash
# Um exercício (Python)
pytest mundo_1_fundamentos/ex001_ola_mundo/

# Um exercício (TypeScript)
npx vitest run mundo_1_fundamentos/ex001_ola_mundo/

# Todos (Python)
pytest

# Todos (TypeScript)
npm test     # ou: npx vitest run
```

## Como usar (TDD)

1. Leia o `README.md` do exercício (spec: Descrição, Parâmetros, Retorno, Exemplos, Restrições).
2. Implemente a função no stub (`solution.py` ou `solution.ts`).
3. Rode os testes do exercício até ficarem verdes.
4. Repita nos próximos.

> Os exercícios interativos (input/print) foram reorganizados como **funções puras** e determinísticas — toda entrada vira parâmetro, toda saída vira retorno. A aleatoriedade e o I/O ficam fora da função testada.

## Como adicionar um exercício novo

Crie a pasta `exNNN_nome/` (ou pasta temática) com os 5 arquivos no padrão:
- `README.md` — spec competitiva
- `solution.py` — função pura tipada (stub)
- `test_solution.py` — `@pytest.mark.parametrize` com casos padrão + edge
- `solution.ts` — `export function nomeCamel(...)` (stub)
- `solution.test.ts` — Vitest com os mesmos casos do pytest

## Exercícios atuais

- **Mundo 1 — Fundamentos:** ex001 … ex035
- **Mundo 2 — Estruturas de Controle:** ex036 … ex071
- **Lógica clássica:** logica/ex01 … ex12 (FizzBuzz, palíndromo, anagrama, two sum, inverter string, contagem de caracteres, maior/menor, soma de dígitos, fatorial, fibonacci, primo, vogais)

(Fonte dos enunciados do lote inicial: **Curso em Vídeo — Gustavo Guanabara**.)

## Licença
MIT