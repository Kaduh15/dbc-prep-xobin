# Exercício 071 — Caixa eletrônico

> Fonte: Curso em Vídeo — Python (Gustavo Guanabara), Mundo 2.

## Descrição

Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.

## Parâmetros e Tipos

- ``valor`` (``int``): valor a ser sacado (inteiro, deve ser >= 0).

## Retorno

``dict[int, int]`` — mapa de cédula -> quantidade, nas denominações ``[100, 50, 20, 10, 5, 2, 1]``, sempre com todas as chaves presentes (quantidade pode ser 0).

## Casos de Exemplo

```
    caixa_eletronico(188) -> {100: 1, 50: 1, 20: 1, 10: 1, 5: 1, 2: 1, 1: 1}
    caixa_eletronico(650) -> {100: 6, 50: 1, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}
    caixa_eletronico(30)  -> {100: 0, 50: 0, 20: 1, 10: 1, 5: 0, 2: 0, 1: 0}
    caixa_eletronico(0)   -> {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}
```

## Casos de Teste (todos, incluindo extremos)

```python
    (188,) -> {100: 1, 50: 1, 20: 1, 10: 1, 5: 1, 2: 1, 1: 1},
    (650,) -> {100: 6, 50: 1, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0},
    (30,) -> {100: 0, 50: 0, 20: 1, 10: 1, 5: 0, 2: 0, 1: 0},
    (0,) -> {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0},
    (100,) -> {100: 1, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0},
    (50,) -> {100: 0, 50: 1, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0},
    (20,) -> {100: 0, 50: 0, 20: 1, 10: 0, 5: 0, 2: 0, 1: 0},
    (10,) -> {100: 0, 50: 0, 20: 0, 10: 1, 5: 0, 2: 0, 1: 0},
    (5,) -> {100: 0, 50: 0, 20: 0, 10: 0, 5: 1, 2: 0, 1: 0},
    (2,) -> {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 1, 1: 0},
    (1,) -> {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 1},
    (8,) -> {100: 0, 50: 0, 20: 0, 10: 0, 5: 1, 2: 1, 1: 1},
    (151,) -> {100: 1, 50: 1, 20: 0, 10: 0, 5: 0, 2: 0, 1: 1},
    (999,) -> {100: 9, 50: 1, 20: 2, 10: 0, 5: 1, 2: 2, 1: 0}
```

## Edge Cases / Extremos

- Algoritmo **guloso**: usa o máximo possível de cada cédula de maior valor.
- Como existe a cédula de ``1``, qualquer inteiro não negativo é totalmente decomposto (todo resto sobra para ``1``).
- Valores **exatos por cédula** (``100``, ``50``, ``20``, ``10``, ``5``, ``2``, ``1``) produzem ``1`` na própria denominação e ``0`` nas demais.
- O mapa retornado sempre contém as **7 denominações**, mesmo com quantidade 0.

## Abordagem / Dica

Itere as denominações em ordem decrescente; para cada ``c`` calcule ``qtd = resto // c`` e atualize ``resto %= c``. O resto residual sempre termina em 0 pela cédula de 1.

## Complexidade

Tempo ``O(7)`` = ``O(1)`` (número fixo de denominações); espaço ``O(7)`` = ``O(1)``.

## Assinatura Canônica

**Python (Pytest):**

```python
from typing import Dict


def caixa_eletronico(valor: int) -> Dict[int, int]:
    raise NotImplementedError
```

**TypeScript (Vitest):**

```ts
export function caixaEletronico(valor: number): Record<number, number> {
    throw new Error("Not implemented");
}
```

> A função é **pura e determinística**: não usa ``input()`` nem ``print()``. A entrada via terminal e a saída na tela ficam fora da função testável.

> Stub para editar: `ex071_caixa_eletronico/solution_ex071_caixa_eletronico.py` (Python) e `solution.ts` (TS).
