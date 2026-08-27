# 🧪 dbc-prep-xobin — Preparação para Testes Técnicos (Vem Ser DBC / Xobin)

Repositório de estudos para **provas técnicas estilo LeetCode/Xobin** (ex.: programa de estágio **Vem Ser DBC**). Os exercícios vêm do **Curso em Vídeo – Python (Gustavo Guanabara)**, **Mundo 1 (Fundamentos)** e **Mundo 2 (Estruturas de Controle)**, convertidos para o formato de programação competitiva — **função pura + casos de teste** — com suporte bilíngue:

- **Python** → Pytest (`solution.py` + `test_solution.py`)
- **TypeScript** → Vitest (`solution.ts` + `solution.test.ts`)

Você escolhe a linguagem: implemente a função no stub e rode os testes. Os enunciados são os **reais** do curso.

## Estrutura

```
dbc-prep-xobin/
├── .github/workflows/tests.yml   # CI: roda pytest e vitest em push/PR
├── mundo_1_fundamentos/
│   └── ex001_deixar_pronto/
│       ├── README.md             # descrição/spec do exercício (estilo competitivo)
│       ├── solution.py           # stub Python
│       ├── test_solution.py      # suíte Pytest (parametrize)
│       ├── solution.ts           # stub TypeScript
│       └── solution.test.ts      # suíte Vitest
├── mundo_2_estruturas_de_controle/
│   └── ex036_emprestimo_bancario/
│       ├── README.md
│       ├── solution.py
│       ├── test_solution.py
│       ├── solution.ts
│       └── solution.test.ts
├── package.json / tsconfig.json / vitest.config.ts   # TS
├── requirements.txt / pytest.ini                     # Python
└── README.md
```

## Pré-requisitos

- **Python 3.10+**
- **Node.js 18+**

## Setup

### Python
```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### TypeScript
```bash
npm install
```

## Como rodar os testes

### Um exercício (Python)
```bash
pytest mundo_1_fundamentos/ex001_deixar_pronto/
```

### Um exercício (TypeScript)
```bash
npx vitest run mundo_1_fundamentos/ex001_deixar_pronto/
```

### Todos (Python)
```bash
pytest
```

### Todos (TypeScript)
```bash
npm test        # ou: npx vitest run
```

## Como usar (TDD)

1. Abra o `README.md` do exercício e leia a spec (Descrição, Parâmetros, Retorno, Exemplos, Restrições).
2. Implemente a função no stub (`solution.py` ou `solution.ts`).
3. Rode os testes do exercício para validar.
4. Rode a suíte completa quando terminar.

> Os exercícios interativos (input/print) do curso foram reorganizados como **funções puras** com parâmetros e retorno tipados. A entrada/saída de terminal fica fora da função testada.

## Exercícios

### Mundo 1 — Fundamentos
`ex001` … `ex035`

### Mundo 2 — Estruturas de Controle
`ex036` … `ex071`

## Licença
MIT