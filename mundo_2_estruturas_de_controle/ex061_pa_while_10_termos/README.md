# Exercício 061 — Progressão aritmética (10 termos) com while

> Fonte: Curso em Vídeo — Python (Gustavo Guanabara), Mundo 2.

## Descrição

Refaça o DESAFIO 051 lendo o primeiro termo e a razão de uma Progressão Aritmética (PA) e exibindo os dez primeiros termos da progressão, agora usando a estrutura de repetição while.

## Parâmetros e Tipos

- ``primeiro`` (``int``): primeiro termo da PA.
- ``razao`` (``int``): razão (passo) entre os termos.

## Retorno

``list[int]`` — lista com os 10 primeiros termos da PA.

## Casos de Exemplo

```
    dez_termos_pa(2, 3)   -> [2, 5, 8, 11, 14, 17, 20, 23, 26, 29]
    dez_termos_pa(1, 1)   -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    dez_termos_pa(10, -2) -> [10, 8, 6, 4, 2, 0, -2, -4, -6, -8]
```

## Casos de Teste (todos, incluindo extremos)

```python
    (2, 3) -> [2, 5, 8, 11, 14, 17, 20, 23, 26, 29],
    (1, 1) -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    (10, -2) -> [10, 8, 6, 4, 2, 0, -2, -4, -6, -8],
    (5, 0) -> [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
    (0, 4) -> [0, 4, 8, 12, 16, 20, 24, 28, 32, 36],
    (-3, -1) -> [-3, -4, -5, -6, -7, -8, -9, -10, -11, -12],
    (7, 2) -> [7, 9, 11, 13, 15, 17, 19, 21, 23, 25]
```

## Edge Cases / Extremos

- A lista deve ter exatamente **10** elementos.
- ``razao == 0``: sequência constante (todos os termos iguais).
- ``razao`` negativa: progressão decrescente.
- ``primeiro`` e/ou ``razao`` negativos: termos podem ficar negativos.
- Termo geral: ``termo_n = primeiro + (n - 1) * razao`` para n de 1 a 10.

## Abordagem / Dica

Gere os 10 índices ``0..9`` e aplique a fórmula ``primeiro + i * razao`` (equivale a ``n = i + 1``). Equivalentemente, itere ``termo`` acumulando a razão a cada passo, mas a forma algébrica é mais simples e evita estado mutável.

## Complexidade

Tempo ``O(10)`` = ``O(1)`` (tamanho fixo); espaço ``O(10)`` = ``O(1)``.

## Assinatura Canônica

**Python (Pytest):**

```python
from typing import List


def dez_termos_pa(primeiro: int, razao: int) -> List[int]:
    raise NotImplementedError
```

**TypeScript (Vitest):**

```ts
export function dezTermosPa(primeiro: number, razao: number): number[] {
    throw new Error("Not implemented");
}
```

> A função é **pura e determinística**: não usa ``input()`` nem ``print()``. A entrada via terminal e a saída na tela ficam fora da função testável.

> Stub para editar: `ex061_pa_while_10_termos/solution_ex061_pa_while_10_termos.py` (Python) e `solution.ts` (TS).
